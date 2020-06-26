## Description

This is a simple REST API / GraphiQL that has as functions to register partners and, calculate which partner is closer, from the geographic coordinates informed by the user.

This API is implemented in production on an EC2 and its database on an RDS on the AWS.

You can access it through the link: http://18.231.49.177:17020/docs or http://18.231.49.177:17020/graphql 

NOTE: The instance is without ssl certificate because I am using the free version.

## Projects Resources

- Languege: Python 3.6
- Package manager: pip
- Main dependencies: [_Flask 1.0.2_](https://flask.palletsprojects.com/en/1.1.x/), [_Flask-Restplus 0.13.0_](https://flask-restplus.readthedocs.io/en/stable/), [_SQLAlchemy 1.3.8_](https://docs.sqlalchemy.org/en/13/orm/tutorial.html), [_Alembic 1.2.1_](https://alembic.sqlalchemy.org/en/latest/tutorial.html), [_Graphene 2.1.8_](https://docs.graphene-python.org/en/latest/), [_Flask-GraphQL 2.0.1_](https://pypi.org/project/Flask-GraphQL/)
- Tests: [_unittest_](https://docs.python.org/3/library/unittest.html)
- DB: [_MySQL 5.7_](https://dev.mysql.com/doc/refman/5.7/en/)

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

The API Doc can be accessed at: http://localhost:5000/docs or http://localhost:5000/graphql

## Running with docker container

Using the docker compose, the web services and database, will be configured and started automatically in the container through the following command line:

`$ docker-compose up`

The API Doc can be accessed at: http://localhost:8000/docs or http://localhost:5000/graphql

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

## To execute tests

`$ FLASK_ENV=development python -m unittest -v`

## Working 

Perform a registration for new partner

- Send a POST request to endpoint: **/partner** with a payload like this JSON:

```javascript
{
    "pdvs": [
        {
            "id": 13,
            "tradingName": "Teste",
            "ownerName": "Teste",
            "document": "00000000000191",
            "coverageArea": {
                "type": "MultiPolygon",
                "coordinates": [
                    [[[-23.562256297264703, -46.66099548339844],
                        [-23.562256297264703, -46.662025451660156],
                        [-23.57358496022532, -46.6644287109375],
                        [-23.58853100613786, -46.65721893310547],
                        [-23.585069967982925, -46.63747787475586],
                        [-23.58082220549596, -46.63061141967774],
                        [-23.568392777659398, -46.631126403808594],
                        [-23.56005338823039, -46.64073944091797],
                        [-23.562256297264703, -46.66099548339844]]],
                    [[[-23.589946859072384, -46.655845642089844],
                        [-23.59167732524408, -46.654987335205085],
                        [-23.59073343743435, -46.655845642089844],
                        [-23.601430434940486, -46.642799377441406],
                        [-23.597969737092242, -46.62185668945313],
                        [-23.589946859072384, -46.622714996337905],
                        [-23.58569925443702, -46.62872314453126],
                        [-23.588688323885066, -46.63970947265626],
                        [-23.589946859072384, -46.655845642089844]]],
                    [[[-23.574686305893117, -46.681766510009766],
                        [-23.584912645897916, -46.682624816894524],
                        [-23.595924736349982, -46.66614532470703],
                        [-23.57924892524502, -46.66322708129883],
                        [-23.57437163664494, -46.68039321899414],
                        [-23.574686305893117, -46.681766510009766]]]
                        ]
                },
            "address": {
                "type": "Point",
                "coordinates": [-23.58748249, -46.67235334]
                }
            }
    ]
}
```

Get a specific partner by id

- send a GET request to endpoint **/partner/{id}** informing the "id" of the registered partner.

```javascript
id = "id of the registered partner"
```

Search the nearest partner with a specifc location coordinates

- send a GET request to endpoint **/partner/{lat}/{lng}**

```javascript
lat = -23.595542907714844
lng = -46.63741527750914
```

Copyright (c) [2020] [Yuri Mussi]