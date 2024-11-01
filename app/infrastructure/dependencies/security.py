from fastapi import Request
from dishka import Provider, provide, Scope

from app.domain.adapters.jwt_token import BaseJWTTokenAdapter
from app.domain.adapters.password_hash import BasePasswordHashAdapter
from app.infrastructure.security.jwt_token import JWTTokenAdapter
from app.infrastructure.security.password_hash import PasswordHashAdapter


class SecurityProvider(Provider):
    
    @provide(scope=Scope.APP)
    def provide_jwt_processor(self) -> BaseJWTTokenAdapter:
        return JWTTokenAdapter()
    
    @provide(scope=Scope.APP)

    def provide_password_hash(self) -> BasePasswordHashAdapter:
        return PasswordHashAdapter()