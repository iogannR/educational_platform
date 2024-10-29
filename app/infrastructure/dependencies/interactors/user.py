from dishka import FromDishka, Provider, Scope, provide

from app.application.use_cases.user import GetAllUsersUseCase
from app.domain.repositories.user import BaseUserRepository


class UserInteractorProvider(Provider):
    
    @provide(scope=Scope.REQUEST)
    async def provide_get_all(
        self,
        user_repository: FromDishka[BaseUserRepository],
    ) -> GetAllUsersUseCase:
        return GetAllUsersUseCase(repository=user_repository)