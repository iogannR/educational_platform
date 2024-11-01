from dishka import FromDishka, Provider, Scope, provide

from app.application.use_cases.user import (
    CreateUserUseCase,
    GetAllUsersUseCase,
    GetUserByIdUseCase,
    GetUserByEmailUseCase,
    DeleteUserUseCase,
)
from app.domain.adapters.password_hash import BasePasswordHashAdapter
from app.domain.repositories.user import BaseUserRepository


class UserInteractorProvider(Provider):
    
    @provide(scope=Scope.REQUEST)
    async def provide_create(
        self,
        user_repository: FromDishka[BaseUserRepository],
        password_hash_adapter: FromDishka[BasePasswordHashAdapter],
    ) -> CreateUserUseCase:
        return CreateUserUseCase(
            repository=user_repository,
            password_hash_adapter=password_hash_adapter,
        )
    
    @provide(scope=Scope.REQUEST)
    async def provide_get_all(
        self,
        user_repository: FromDishka[BaseUserRepository],
    ) -> GetAllUsersUseCase:
        return GetAllUsersUseCase(repository=user_repository)
    
    @provide(scope=Scope.REQUEST)
    async def provide_get_by_id(
        self,
        user_repository: FromDishka[BaseUserRepository],
    ) -> GetUserByIdUseCase:
        return GetUserByIdUseCase(repository=user_repository)
    
    @provide(scope=Scope.REQUEST)
    async def provide_get_by_email(
        self,
        user_repository: FromDishka[BaseUserRepository],
    ) -> GetUserByEmailUseCase:
        return GetUserByEmailUseCase(repository=user_repository)
    
    @provide(scope=Scope.REQUEST)
    async def provide_delete(
        self,
        user_repository: FromDishka[BaseUserRepository],
    ) -> DeleteUserUseCase:
        return DeleteUserUseCase(repository=user_repository)