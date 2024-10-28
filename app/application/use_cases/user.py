from app.application.dto.user import UserResponse
from app.application.use_cases.interactor import Interactor
from app.domain.entities.user import UserEntity
from app.domain.repositories.user import BaseUserRepository


class GetAllUsersUseCase(Interactor[None, UserResponse]):
    def __init__(self, repository: BaseUserRepository) -> None:
        self._repository = repository
    
    async def __call__(self, request: None = None) -> list[UserResponse]:
        entities: list[UserEntity] = await self._repository.get_all()
        return [UserResponse.from_entity(entity) for entity in entities]