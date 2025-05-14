from fastapi import FastAPI
from app.api.routes.board import router
from fastapi.testclient import TestClient

import pytest


@pytest.fixture
def client():
    game = FastAPI()
    game.include_router(router, prefix="/board")
    return TestClient(game)


def test_if_initial_state_is_empty_board(client):
    response = client.get("/board")
    assert response.status_code == 200
    assert response.json() == {"grid": [[" " for i in range(3)] for i in range(3)]}
