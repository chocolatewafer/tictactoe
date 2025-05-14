# from fastapi import FastAPI
from app.main import app
from fastapi.testclient import TestClient

import pytest


@pytest.fixture
def client():
    return TestClient(app)


def test_if_initial_state_is_empty_board(client):
    response = client.get("/api/v1/board")
    assert response.status_code == 200
    assert response.json() == {
        "grid": [[" " for i in range(3)] for i in range(3)],
        "player_turn": "o",
    }


def test_first_player_move(client):
    response = client.post("/api/v1/board", json={"row": 2, "col": 2})
    assert response.status_code == 200
    assert response.json() == "player o added to 2,2"
