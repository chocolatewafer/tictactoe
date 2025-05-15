# tictactoe

This is a FAST API project that serves tictactoe game using api calls

- github: https://github.com/chocolatewafer/tictactoe

- videolink:

**mkdocs** are available too, clone and serve please.

## Development Requirements

- Python 3.11+


## Installation

```sh
python -m venv venv
venv/bin/activate
pip install -r requirements.txt
```

## Runnning Localhost

`make run`

## Deploy app

`make deploy`

## Running Tests

`make test`

## Access Swagger Documentation

> <http://localhost:8080/docs>

## Access Redocs Documentation

> <http://localhost:8080/redoc>

## Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:

```
└── 📁tictactoe
        └── 📁hooks
            └── pre-commit
    └── 📁.github
        └── 📁workflows
            └── ci.yaml
    └── 📁app
        └── __init__.py
        └── 📁api
            └── __init__.py
            └── 📁routes
                └── __init__.py
                └── api.py
                └── board.py
        └── 📁core
            └── __init__.py
            └── config.py
            └── logging.py
        └── main.py
    └── 📁docs
        └── index.md
    └── 📁tests
        └── __init__.py
        └── test_board_router.py
    └── .dockerignore
    └── .env
    └── .gitignore
    └── .pre-commit-config.yaml
    └── .pylintrc
    └── docker-compose.yml
    └── Dockerfile
    └── Makefile
    └── mkdocs.yml
    └── README.md
    └── requirements.txt
    └── uv.lock
```
