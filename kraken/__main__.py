import asyncio
import logging

from hypercorn.asyncio import serve
from hypercorn.config import Config

from kraken.app import create_app
from kraken.settings import settings
from kraken.utils.logging_loader import init_logging

if __name__ == "__main__":
    init_logging()

    logger = logging.getLogger(__name__)

    config = Config()
    config.workers = settings.WORKERS
    config.debug = settings.DEBUG
    config.bind = [settings.BIND]
    config.accesslog = logger

    asyncio.run(serve(create_app(), config, mode="asgi"))
