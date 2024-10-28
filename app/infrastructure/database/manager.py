from asyncio import current_task
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncEngine,
    AsyncSession,
)

from app.infrastructure.config import settings


class DatabaseManager:
    def __init__(
        self,
        url: str,
        echo: bool = settings.db.echo,
        pool_size: int = settings.db.pool_size,
        max_overflow: int = settings.db.max_overflow,
    ) -> None:
        self._engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self._session_factory: async_scoped_session[
            async_sessionmaker[AsyncSession]
        ] = async_scoped_session(
            async_sessionmaker(
                bind=self._engine,
                autoflush=False,
                expire_on_commit=False,
                future=True,
            ),
            scopefunc=current_task,
        )
        
    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        session: AsyncSession = self.session_factory()
        try:
            yield session
        except IntegrityError as exception:
            await session.rollback()
        finally:
            await session.close()