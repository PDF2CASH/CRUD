[![Build Status](https://travis-ci.org/PDF2CASH/PDF2CASH_IdentityManagement.svg?branch=development)](https://travis-ci.org/PDF2CASH/PDF2CASH_IdentityManagement)
[![Coverage Status](https://coveralls.io/repos/github/PDF2CASH/PDF2CASH_IdentityManagement/badge.svg?branch=development)](https://coveralls.io/github/PDF2CASH/PDF2CASH_IdentityManagement?branch=development)
# PDF2CASH_APIGateway

## Iniciando usando docker

### Pré-requisitos

A fim de conseguir iniciar o serviço, os seguintes pacotes são necessários:

  -  docker
  -  docker-compose

Caso esteja usando uma plataforma linux, verifique na documentação de sua distro, como obter os referidos pacotes.

### Instalando

Construa os containers:
```bash
docker-compose build
```
### Uso

Execute o compose:
```bash
docker-compose up
```

O comando acima irá deixar o container rodando o servidor e escutando pela porta 8000

```bash
http://localhost:8000/
```

## Contribuindo

Por favor leia o nosso [CONTRIBUTING.md](https://github.com/fga-eps-mds/2018.2-PDF2CASH/blob/master/CONTRIBUTING.md) se deseja contribuir com nosso projeto.

## Licensa

Esse projeto é licensiado sobre a licensa MIT
