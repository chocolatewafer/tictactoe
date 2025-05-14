from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/board", tags=["board"])

game_board = {
    "grid": [[" " for i in range(3)] for i in range(3)],
    "player_turn": "o",
    "player_win": None,
}


class Board(BaseModel):
    grid: list[list[str]]
    player_turn: str
    player_win: str | None


class player_move(BaseModel):
    row: int
    col: int


@router.get("/")
async def get_board() -> Board:
    return game_board


@router.post("/")
async def put_board(move: player_move):
    row = move.row
    col = move.col
    player_turn = game_board["player_turn"]
    game_board["grid"][row][col] = player_turn
    if game_board["player_turn"] == "o":
        game_board.update({"player_turn": "x"})
    else:
        game_board.update({"player_turn": "o"})
    return f"player {player_turn} added to {row},{col}"


@router.post("/reset")
async def new_board() -> str:
    game_board.update(
        {
            "grid": [[" " for i in range(3)] for i in range(3)],
            "player_turn": "o",
            "player_win": None,
        }
    )
    return "new game created"
