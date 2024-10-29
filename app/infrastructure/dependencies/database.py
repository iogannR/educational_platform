from typing import AsyncIterable

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
    AsyncSession
)
from dishka import Provider, provide, Scope
from dishka.integrations.fastapi import FromDishka

from app.infrastructure.config import settings


class DatabaseProvider(Provider):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url
        
    @provide(scope=Scope.APP)
    async def provide_engine(self) -> AsyncEngine:
        return create_async_engine(
            url=self.url,
            echo=settings.db.echo,
            pool_size=settings.db.pool_size,
            max_overflow=settings.db.max_overflow,
        )
        
    @provide(scope=Scope.APP)
    def provide_sessionmaker(
        self, engine: FromDishka[AsyncEngine],
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            bind=engine,
            autoflush=False,
            expire_on_commit=False,
            future=True,
        )
        
    @provide(scope=Scope.APP)
    async def provide_session(
        self, session_maker: FromDishka[async_sessionmaker[AsyncSession]],
    ) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session