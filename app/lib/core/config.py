import os
from datetime import datetime
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings


def get_path(path_type: str) -> str:
    """
    reduces a bit of repetitive code
    """
    path = os.path.join(os.path.dirname(__file__), "../..")

    if path_type == "docs":
        path = os.path.join(path, "docs")

    return os.path.abspath(path=path)


class Settings(BaseSettings):
    """
    Type declarations & default values for settings
    """

    # General
    API_NAME: str = "Activity Tracker Management API"
    API_V1_PREFIX: str = "/api/v1"
    API_PORT: int = 5000
    API_HOST: str = "0.0.0.0"
    API_BOOT_TIME: datetime = datetime.utcnow()

    # Date / Time Formats
    DATETIME_FORMAT: str

    # Paths
    BASE_DIR: str = get_path("base")
    DOCS_DIR: str = get_path("docs")

    # Logging
    LOG_FILE: str
    LOG_LEVEL: str
    LOGGER_NAME: str = "management_api"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    # Development Assistance
    RELOAD: bool = False

    # Database
    MONGODB_HOSTS: str
    MONGODB_DBNAME: str
    MONGODB_USER: Optional[str]
    MONGODB_PORT: int
    MONGODB_MONITORING: bool = False

    # DB_COLLECTIONS_TO_SKIP: List[str]
    DB_STATS_SCALE: int = 1024 * 1024

    # CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    class Config:  # pylint: disable=too-few-public-methods
        """
        Specifies the local config file
        """
        env_file = ".env"


if os.getenv("TESTING"):
    settings = Settings(
        LOG_FILE="/tmp/foo.log",
        MONGODB_DBNAME="management_api",
        API_PORT=9999,
        LOG_LEVEL="DEBUG",
        MONGODB_HOSTS="localhost",
        MONGODB_PORT=27017
    )
else:
    settings = Settings()