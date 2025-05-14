from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/board", tags=["board"])

game_board = {"grid": [[" " for i in range(3)] for i in range(3)], "player_turn": "o"}


class Board(BaseModel):
    grid: list[list[str]]
    player_turn: str


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
    game_board["grid"][row][col] = "o"
    return f"player o added to {row},{col}"


@router.post("/reset")
async def new_board() -> str:
    game_board.update(
        {"grid": [[" " for i in range(3)] for i in range(3)], "player_turn": "o"}
    )
    return "new game created"
