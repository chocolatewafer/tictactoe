from fastapi import APIRouter, HTTPException
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


def winlogic(gameboard):
    print(gameboard)
    if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] != " ":
        return True

    if gameboard[0][2] == gameboard[1][1] == gameboard[2][2] != " ":
        return True

    for i in range(3):
        if gameboard[i][0] == gameboard[i][1] == gameboard[i][2] != " ":
            return True

    for i in range(3):
        if gameboard[0][i] == gameboard[1][i] == gameboard[2][i] != " ":
            return True
    return False


@router.get("/")
async def get_board() -> Board:
    return game_board


@router.post("/")
async def put_board(move: player_move) -> list:
    if game_board["player_win"]:
        raise HTTPException(status_code=400, detail="Game is already over!")

    row = move.row
    col = move.col

    if not (0 <= row <= 2 and 0 <= col <= 2):
        raise HTTPException(
            status_code=400, detail="row and col must be between 0 and 2"
        )

    if game_board["grid"][row][col] != " ":
        raise HTTPException(
            status_code=400, detail="This cell is already filled. Choose another one"
        )

    player_turn = game_board["player_turn"]
    game_board["grid"][row][col] = player_turn
    won = winlogic(game_board["grid"])
    if won:
        game_board["player_win"] = player_turn
        return [f"player {player_turn} Won!", game_board]
    if game_board["player_turn"] == "o":
        game_board.update({"player_turn": "x"})
    else:
        game_board.update({"player_turn": "o"})
    return [f"player {player_turn} added to {row},{col}", game_board]


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
