from fastapi import APIRouter

from api.routes import board

router = APIRouter()
router.include_router(board.router, tags=["board"], prefix="/v1")
