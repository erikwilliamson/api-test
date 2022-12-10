import logging

from app.lib.core import settings

logger = logging.getLogger(settings.LOGGER_NAME)


async def db_connectivity_check() -> str:
    conn = connection.get_connection()
    try:
        _ = conn.server_info()
    except connection.ConnectionFailure:
        return "FAILED"
    else:
        return "PASSED"
