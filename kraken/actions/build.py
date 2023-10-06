import logging

from aioka.handler import BaseHandler
from aioka.server import BaseMeta
from pydantic import BaseModel

handler = BaseHandler()

logger = logging.getLogger(__name__)


@handler.action("build_status")
async def build_web(meta: BaseMeta, payload: BaseModel) -> dict:
    logger.info("meta=%s", meta)
    logger.info("payload=%s", payload)
    return {}
