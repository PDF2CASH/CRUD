from django.test import TestCase
from .models import Worker
import json

# Create your tests here.


class WorkerTest(TestCase):
    url = '/api/worker/worker/'

    def setUp(self):
        self.worker1 = Worker.objects.create_user(
            username='aloaloalo',
            cpf='94837284799',
            email='carlosalberto@email.com',
            password='12345678'
        )
        response = self.client.post('/api/authenticate/', {
            'username': 'aloaloalo',
            'password': '12345678'
        })

        self.token = json.loads(response.content)['token']

    def as_dict(self):
        return {
            'id': self.worker1.id,
            'username': self.worker1.username,
            'cpf': self.worker1.cpf,
            'email': self.worker1.email,
            'password': self.worker1.password
        }

    def test_worker_object_get(self):
        response = self.client.get(
            self.url,
            HTTP_AUTHORIZATION='JWT {}'.format(self.token)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), 1)

    def test_worker_object_post(self):
        data = {
            'username': 'aloaloaloalo',
            'cpf': '94831284799',
            'email': 'carlosalberto@email.com',
            'password': '123456789'
        }
        response = self.client.post(
            self.url,
            data,
            HTTP_AUTHORIZATION='JWT {}'.format(self.token)
        )
        self.assertEqual(response.status_code, 201)
        data['id'] = json.loads(response.content)['id']
        self.assertEqual(json.loads(response.content), data)

    def test_worker_object_delete(self):
        self.url += f'{self.worker1.id}/'
        response = self.client.delete(
            self.url,
            HTTP_AUTHORIZATION='JWT {}'.format(self.token)
        )
        self.assertEqual(response.status_code, 204)

    def test_worker_object_read(self):
        self.url += f'{self.worker1.id}/'
        response = self.client.get(
            self.url,
            HTTP_AUTHORIZATION='JWT {}'.format(self.token)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), self.as_dict())

    def test_worker_object_partial_update(self):
        self.url += f'{self.worker1.id}/'
        data = {
            'id': self.worker1.id,
            'username': 'aloaloaaaaaa',
            'cpf': '27491047355',
            'email': 'robertojunior@email.com',
            'password': '483058492'
        }
        response = self.client.post(
            self.url,
            data,
            HTTP_AUTHORIZATION='JWT {}'.format(self.token)
        )
        self.assertEqual(response.status_code, 200)

    def test_refresh_jwt_token(self):

        response = self.client.post('/api/refresh/', {
            'token': self.token,
        })

        self.assertIsInstance(json.loads(response.content), dict)

    def tearDown(self):
        Worker.objects.all().delete()
