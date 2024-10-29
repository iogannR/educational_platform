from uuid import UUID

from app.application.dto.user import UserCreate, UserResponse
from app.application.use_cases.interactor import Interactor
from app.domain.entities.user import UserEntity
from app.domain.repositories.user import BaseUserRepository


class CreateUserUseCase(Interactor[UserCreate, UserResponse]):
    def __init__(self, repository: BaseUserRepository) -> None:
        self._repository = repository
    
    async def __call__(self, request: UserCreate) -> UserResponse:
        params_entity = request.to_entity()
        entity: UserEntity = await self._repository.create(params_entity)
        return UserResponse.from_entity(entity)
    

class GetAllUsersUseCase(Interactor[None, UserResponse]):
    def __init__(self, repository: BaseUserRepository) -> None:
        self._repository = repository
    
    async def __call__(self, request: None = None) -> list[UserResponse]:
        entities: list[UserEntity] = await self._repository.get_all()
        return [UserResponse.from_entity(entity) for entity in entities]
    
    
class GetUserByIdUseCase(Interactor[UUID, UserResponse]):
    def __init__(self, repository: BaseUserRepository) -> None:
        self._repository = repository
    
    async def __call__(self, request: UUID) -> UserResponse | None:
        entity: UserEntity | None = await self._repository.get_by_id(request)
        if not entity:
            return None
        return UserResponse.from_entity(entity)
    

class GetUserByEmailUseCase(Interactor[str, UserResponse]):
    def __init__(self, repository: BaseUserRepository) -> None:
        self._repository = repository
        
    async def __call__(self, request: str) -> UserResponse | None:
        entity: UserEntity | None = await self._repository.get_by_email(request)
        if not entity:
            return None
        return UserResponse.from_entity(entity)
    
    
class DeleteUserUseCase(Interactor[UUID, None]):
    def __init__(self, repository: BaseUserRepository) -> None:
        self._repository = repository
        
    async def __call__(self, request: UUID) -> None:
        return await self._repository.delete(request)