import logging
import sys

from app.core.logging import InterceptHandler
from loguru import logger
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

API_PREFIX = "/api"
VERSION = "0.1.10"
DEBUG: bool = config("DEBUG", cast=bool, default=False)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="")
PROJECT_NAME: str = config("PROJECT_NAME", default="tictactoe")

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
