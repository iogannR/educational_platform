from typing import Protocol

from app.domain.entities.user import UserEntity


class BaseUserRepository(Protocol):
    """
    Base user repository protocol, from which database user repository should be inherited
    """
    
    async def create(self, entity: UserEntity) -> UserEntity:
        raise NotImplementedError()
    
    async def get_all(self) -> list[UserEntity]:
        raise NotImplementedError()
    
    async def get_by_email(self) -> UserEntity | None:
        raise NotImplementedError()
    
    async def get_by_id(self) -> UserEntity | None:
        raise NotImplementedError()
    
    async def delete(self) -> None:
        raise NotImplementedError()