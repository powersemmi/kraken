from typing import Annotated

from pydantic.networks import MultiHostUrl, UrlConstraints

AsyncPostgresDsn = Annotated[
    MultiHostUrl,
    UrlConstraints(
        host_required=True,
        allowed_schemes=["postgresql+asyncpg"],
    ),
]
