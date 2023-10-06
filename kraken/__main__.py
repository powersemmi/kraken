import asyncio
import logging

import click
from aioka.server.app import AsyncApp

from kraken.actions import build
from kraken.utils.logging_loader import init_logging

logger = logging.getLogger()


async def main():
    from aioka.server.app import create_app
    from aioka.server.master import AsyncRqMasterServer

    from kraken.app import create_app as create_asgi_app
    from kraken.settings import settings

    log_config = init_logging()

    host, port = settings.BIND.split(":")

    app: AsyncApp
    async with create_app(
        service_name=settings.SERVICE_NAME.lower(),
        rmq_urls=[str(i) for i in settings.RMQ_URLS],
        exchange=settings.EXCHANGE,
    ) as app:
        app.add_handler(build.handler)
        app.add_uvicorn_asgi(
            create_asgi_app(), host=host, port=int(port), log_config=log_config
        )


@click.group()
def cls():
    ...


@click.command()
def run_server():
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()


cls.add_command(run_server)

if __name__ == "__main__":
    cls()
