from dataclasses import asdict

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.user import UserEntity
from app.domain.repositories.user import BaseUserRepository
from app.domain.value_objects.idvo import IdVO
from app.infrastructure.database.models.user import User


class UserSQLAlchemyRepository(BaseUserRepository):
    """User SQLAlchemy Repository implementation"""
    
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        
    async def create(self, entity: UserEntity) -> UserEntity:
        user: User = User(**asdict(entity))
        self._session.add(user)
        await self._session.commit()
        await self._session.refresh(user)
        return user.to_entity()
        
    async def get_all(self) -> list[UserEntity]:
        stmt = select(User).order_by(User.id)
        result: Result = await self._session.execute(stmt)
        entities: list[User] = result.scalars().all()
        return [user.to_entity() for user in entities]
        
    async def get_by_id(self, id_: IdVO) -> UserEntity | None:
        user: User | None = await self._session.get(User, id_)
        if not user:
            return None
        return user.to_entity()
        
    async def get_by_email(self, email: str) -> UserEntity | None:
        user: User | None = await self._session.get(User, email)
        if not user:
            return None
        return user.to_entity()
        
    async def delete(self, id_: IdVO) -> None:
        user: User | None = await self._session.get(User, id_)
        await self._session.delete(user)
        await self._session.execute
        return