from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/board")

game_board = {"grid": [[" " for i in range(3)] for i in range(3)]}


class Board(BaseModel):
    grid: list[list[str]]
