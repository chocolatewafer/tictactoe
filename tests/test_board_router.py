from fastapi import HTTPException
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
    assert response.json()[0] == "player o added to 2,2"


def test_reset_game_board(client):
    response = client.post("/api/v1/board", json={"row": 2, "col": 2})
    assert response.status_code == 200
    assert response.json()[0] == "player o added to 2,2"
    response = client.post("/api/v1/board/reset")
    assert response.status_code == 200
    assert response.json() == "new game created"


def test_player_turn_change(client):
    response = client.post("/api/v1/board", json={"row": 1, "col": 1})
    assert response.status_code == 200
    assert response.json()[0] == "player o added to 1,1"
    response = client.post("/api/v1/board", json={"row": 2, "col": 2})
    assert response.status_code == 200
    assert response.json()[0] == "player x added to 2,2"


def test_win_condition(client):
    response = client.post("/api/v1/board", json={"row": 0, "col": 0})
    assert response.status_code == 200
    response = client.post("/api/v1/board", json={"row": 1, "col": 0})
    assert response.status_code == 200
    response = client.post("/api/v1/board", json={"row": 0, "col": 1})
    assert response.status_code == 200
    response = client.post("/api/v1/board", json={"row": 1, "col": 1})
    assert response.status_code == 200
    response = client.post("/api/v1/board", json={"row": 0, "col": 2})
    assert response.status_code == 200
    response_text = response.json()
    assert response_text[0] == "player o Won!"
    assert response_text[1]["player_win"] == "o"


def test_index_out_of_range(client):
    response = client.post("/api/v1/board", json={"row": 3, "col": 0})
    assert response.status_code == 400
    assert response.json()["detail"] == "row and col must be between 0 and 2"


def test_input_in_same_cell(client):
    client.post("/api/v1/board", json={"row": 1, "col": 1})
    response = client.post("/api/v1/board", json={"row": 1, "col": 1})
    assert response.status_code == 400
    assert (
        response.json()["detail"] == "This cell is already filled. Choose another one"
    )


def test_game_already_over_and_input(client):
    # NOTE: do we have to assert status code each time or is it better to leave it out
    client.post("/api/v1/board", json={"row": 0, "col": 0})
    client.post("/api/v1/board", json={"row": 1, "col": 0})
    client.post("/api/v1/board", json={"row": 0, "col": 1})
    client.post("/api/v1/board", json={"row": 1, "col": 1})
    client.post("/api/v1/board", json={"row": 0, "col": 2})
    response = client.post("/api/v1/board", json={"row": 0, "col": 2})
    assert response.status_code == 400
    assert response.json()["detail"] == "Game is already over!"
