from collections.abc import Generator
from functools import lru_cache

from sqlalchemy import Engine
from sqlmodel import Session, create_engine

from .config import get_settings


@lru_cache
def get_engine() -> Engine:
    """One engine (and connection pool) for the whole app."""
    return create_engine(get_settings().database_url)


def get_session() -> Generator[Session]:
    """Give each request its own session and close it afterwards,
    even when the request fails."""
    with Session(get_engine()) as session:
        yield session
