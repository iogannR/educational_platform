from dishka import make_async_container, AsyncContainer

from app.infrastructure.dependencies.database import DatabaseProvider
from app.infrastructure.dependencies.interactors.user import UserInteractorProvider
from app.infrastructure.dependencies.repositories import RepositoryProvider
from app.infrastructure.config import settings


def create_async_container(url: str) -> AsyncContainer:
    container = make_async_container(
        DatabaseProvider(url=url),
        RepositoryProvider(),
        UserInteractorProvider(),
    )
    
    return container