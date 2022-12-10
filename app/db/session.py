import logging
from beanie import init_beanie

from pymongo import monitoring
import motor.motor_asyncio

from app.lib.core import settings

logger = logging.getLogger(settings.LOGGER_NAME)


class CommandLogger(monitoring.CommandListener):
    def started(self, event: monitoring.CommandStartedEvent) -> None:
        logger.debug(
            "Command %s with request id %s started on server %s",
            event.command_name,
            event.request_id,
            event.connection_id,
        )
        logger.debug("Command is %s", event.command)

    def succeeded(self, event: monitoring.CommandSucceededEvent) -> None:
        logger.debug(
            "Command %s with request id %s on server %s succeeded in %s microseconds",
            event.command_name,
            event.request_id,
            event.connection_id,
            event.duration_micros
        )

    def failed(self, event: monitoring.CommandFailedEvent) -> None:
        logger.debug(
            "Command %s with request id %s on server %s failed in %s microseconds",
            event.command_name,
            event.request_id,
            event.connection_id,
            event.duration_micros
        )


async def mongo_connect() -> None:
    if settings.MONGODB_MONITORING:
        monitoring.register(CommandLogger())

    mongo_uri = get_mongo_uri(
        hosts=settings.MONGODB_HOSTS,
        port=settings.MONGODB_PORT
    )

    logger.info("Connecting to mongo at %s", mongo_uri)
    client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
    logger.info("Connected to mongo")

    logger.info("Initializing Beanie")
    await init_beanie(
        database=client[settings.MONGODB_DBNAME],
        document_models=[
            "app.lib.models.company.Company",
            "app.lib.models.pet.Pet",
            "app.lib.models.car.Car"
        ]
    )
    logger.info("Beanie initialization complete")


async def close_mongo() -> None:
    # TODO: what is the proper way to disconnect?
    logger.info("Disconnecting from mongo instance")


async def get_session() -> None:
    # TODO: is this needed?
    return


def get_mongo_uri(hosts: str, port: int) -> str:
    # Hosts is a comma-separated list of hosts. Explode it and insert ports.
    ported_hosts = [f"{host}:{port}" for host in hosts.split(",")]
    cluster = ",".join(ported_hosts)

    return f"mongodb://{cluster}"
