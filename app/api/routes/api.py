from fastapi import APIRouter

from app.api.routes import board

router = APIRouter(prefix="/v1")
router.include_router(board.router)
