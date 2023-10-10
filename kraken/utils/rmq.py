from faststream.rabbit import RabbitExchange, ExchangeType

from kraken.settings import settings

default_exchange = RabbitExchange(
    settings.EXCHANGE, auto_delete=True, type=ExchangeType.TOPIC
)
