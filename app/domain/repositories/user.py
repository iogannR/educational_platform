from typing import Protocol

from app.domain.entities.user import UserEntity
from app.domain.value_objects.idvo import IdVO


class BaseUserRepository(Protocol):
    """
    Base Protocol, from which User Repository implementation should be inherited
    """
    
    async def create(self, entity: UserEntity) -> UserEntity:
        raise NotImplementedError()
    
    async def get_all(self) -> list[UserEntity]:
        raise NotImplementedError()
    
    async def get_by_id(self, id_: IdVO) -> UserEntity | None:
        raise NotImplementedError()
    
    async def get_by_email(self, email: str) -> UserEntity | None:
        raise NotImplementedError()
    
    async def delete(self, id_: IdVO) -> None:
        raise NotImplementedError()