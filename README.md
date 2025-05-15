# tictactoe

This is a FAST API project that serves tictactoe game using api calls

## Development Requirements

- Python 3.11+
- Uv (Python Package Manager)

## Installation

```sh
python -m venv venv
source venv/bin/activate
make install
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
    app
    └── 📁tictactoe
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
                    └── predictor.py
            └── 📁core
                └── __init__.py
                └── config.py
                └── errors.py
                └── events.py
                └── logging.py
                └── paginator.py
            └── main.py
        └── 📁tests
            └── __init__.py
            └── test_pagination_behavior.py
        └── .env.example
        └── .gitignore
        └── .pre-commit-config.yaml
        └── .pylintrc
        └── docker-compose.yml
        └── Dockerfile
        └── Makefile
        └── pyproject.toml
        └── README.md
        └── uv.lock
```
