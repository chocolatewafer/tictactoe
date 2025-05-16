# tictactoe

## PREFACE
I had to choose a project to implement for the fellowship to learn 12 Factor App development along with FastAPI, Dockerization and CI/CD. So I chose to make a simple tictactoe application that can be played using endpoints.

---

## More Thoughts

During the beginning of this endeavour I thought I would try making an AI app itself that was served using FAST API endpoints.

The problem was I did not know how to use FAST API (only know REST API and am familiar with Django) and had no idea on CI/CD and Dockerization. The task became daunting pretty soon once I started setting up the project.

So I changed my approach to try and make the simplest app I could with very basic logic, that would give me enough challenges to learn the very basics of FastAPI, Docker, GithubActions and 12 Factor app development- the tictactoe we all once played on the bench during class lectures in 5th grade.

And so here we are. This is the mkdocs serving; the cherry on the top of the project. I have listed the project structure and the setup of the project for anyone who is reviewing this bad boy piece of fresher code pile:

---

## Project layout
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
---

## Installation

```
git clone https://github.com/chocolatewafer/tictactoe
pip install -r requirements.txt
```
To test the fastapi application:
```
fastpi dev
```
To serve mkdocs ( This one is easy ):
```
mkdocs serve
```
Dockerization is not added to CI/CD yet. Do it manually.
