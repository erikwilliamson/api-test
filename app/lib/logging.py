from pydantic import BaseModel
from app.lib.core import settings
from logging.config import dictConfig


class LogConfig(BaseModel):
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": settings.LOG_FORMAT,
            "datefmt": settings.LOG_DATETIME_FORMAT
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr"
        }
    }
    loggers = {
        settings.LOGGER_NAME: {"handlers": ["default"], "level": settings.LOG_LEVEL}
    }


def init_logging():
    dictConfig(LogConfig().dict())
