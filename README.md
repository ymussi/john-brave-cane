## Description

This is a simple REST API that has as functions to register partners and, calculate which partner is closer, from the geographic coordinates informed by the user.

## Projects Resources

- Languege: Python 3.6
- Package manager: pip
- Main dependencies: Flask 1.0.2, Flask-Restplus 0.13.0, SQLAlchemy 1.3.8, Alembic 1.2.1
- Tests: Unittest
- DB: MySQL 5.7

## Installation

First of all, clone this project in your work environment.

`$ git clone https://github.com/ymussi/john-brave-cane.git`

and after that choice your runing method:

## Running out of docker container

```bash
$ pip install -r requirements.txt
$ python setup.py develop
$ cd brave_cane/
$ python run.py
```

The API Doc can be accessed at: http://localhost:5000/docs

## Running with docker container

Using the docker compose, the web services and database, will be configured and started automatically in the container through the following command line:

`$ docker-compose up`

The API Doc can be accessed at: http://localhost:8000/docs

## Database Server

The database server will be exposed externally on:

- host: localhost
- username: brave
- password: brave
- port: 23307
-   database: brave_cane


## Runing migrations

```bash
$ cd brave_cane/
$ alembic upgrade head
```

## To Test

`$ FLASK_ENV=development python -m unittest -v`