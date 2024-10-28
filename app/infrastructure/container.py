from dependency_injector import providers, containers

from app.application.use_cases.user import GetAllUsersUseCase
from app.infrastructure.database.manager import DatabaseManager
from app.infrastructure.config import settings
from app.infrastructure.repositories.user import UserSQLAlchemyRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["app.api.routes"],
    )
    
    db = providers.Singleton(DatabaseManager, url=str(settings.db.url))
    
    user_repository = providers.Factory(
        UserSQLAlchemyRepository,
        session=db.provided.session(),
    )
    
    get_all_users_use_case = providers.Factory(
        GetAllUsersUseCase,
        repository=user_repository,
    )