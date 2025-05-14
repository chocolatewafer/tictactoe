# from fastapi import FastAPI
from app.main import app
from fastapi.testclient import TestClient

import pytest


@pytest.fixture
def client():
    game = TestClient(app)
    game.post("/api/v1/board/reset")
    return game


def test_if_initial_state_is_empty_board(client):
    response = client.get("/api/v1/board")
    assert response.status_code == 200
    assert response.json() == {
        "grid": [[" " for i in range(3)] for i in range(3)],
        "player_turn": "o",
        "player_win": None,
    }


def test_first_player_move(client):
    response = client.post("/api/v1/board", json={"row": 2, "col": 2})
    assert response.status_code == 200
    assert response.json() == "player o added to 2,2"


def test_reset_game_board(client):
    response = client.post("/api/v1/board", json={"row": 2, "col": 2})
    assert response.status_code == 200
    assert response.json() == "player o added to 2,2"
    response = client.post("/api/v1/board/reset")
    assert response.status_code == 200
    assert response.json() == "new game created"


def test_player_turn_change(client):
    response = client.post("/api/v1/board", json={"row": 1, "col": 1})
    assert response.status_code == 200
    assert response.json() == "player o added to 1,1"
    response = client.post("/api/v1/board", json={"row": 2, "col": 2})
    assert response.status_code == 200
    assert response.json() == "player x added to 2,2"
