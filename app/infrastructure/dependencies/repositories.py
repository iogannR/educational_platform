from sqlalchemy.ext.asyncio import AsyncSession
from dishka import FromDishka, Provider, Scope, provide

from app.domain.repositories.user import BaseUserRepository
from app.infrastructure.repositories.user import UserSQLAlchemyRepository


class RepositoryProvider(Provider):
    
    @provide(scope=Scope.REQUEST)
    async def provide_user_repository(
        self, 
        session: FromDishka[AsyncSession],
    ) -> BaseUserRepository:
        return UserSQLAlchemyRepository(session=session)