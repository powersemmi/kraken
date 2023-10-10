import logging

from faststream.rabbit.fastapi import RabbitRouter

from kraken.settings import settings
from kraken.utils.rmq import default_exchange

router = RabbitRouter(
    str(settings.RMQ_URL),
    schema_url="/asyncapi",
    include_in_schema=True,
    setup_state=False,  # type: ignore[call-arg]
)

logger = logging.getLogger(__name__)


@router.subscriber("build_status", exchange=default_exchange)
async def build_status() -> dict:
    return {}
