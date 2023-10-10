from pydantic import AmqpDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

from kraken.utils.types import AsyncPostgresDsn


class Settings(BaseSettings):
    # Rabbit
    RMQ_URL: AmqpDsn
    EXCHANGE: str = "services"

    # Postgres
    PG_DSN: AsyncPostgresDsn

    # Service
    SERVICE_NAME: str = "kraken"
    BIND: str = "0.0.0.0:8080"
    DEBUG: bool = False
    WORKERS: int = 1

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )


settings = Settings()
