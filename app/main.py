import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.lib.core.config import settings
from app.db.session import mongo_connect, close_mongo
from app.lib.logging import init_logging
from app.lib.exceptions import ConfigException
import sys

try:
    init_logging()
except ConfigException as exc:
    print(exc.message)
    sys.exit(exc.exit_code)

logger = logging.getLogger(settings.LOGGER_NAME)
logger.info("Welcome to the Activity Tracker Management API")

app = FastAPI(
    title=settings.API_NAME, openapi_url=f"{settings.API_V1_PREFIX}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_PREFIX)

app.add_event_handler("startup", mongo_connect)
app.add_event_handler("shutdown", close_mongo)
