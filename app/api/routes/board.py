from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/board", tags=["board"])

game_board = {"grid": [[" " for i in range(3)] for i in range(3)], "player_turn": "o"}


class Board(BaseModel):
    grid: list[list[str]]


@router.get("/")
async def get_board():
    return game_board
