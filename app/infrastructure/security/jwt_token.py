import uuid
from datetime import UTC, datetime, timedelta

import jwt

from app.domain.adapters.jwt_token import BaseJWTTokenAdapter
from app.infrastructure.config import settings


class JWTTokenAdapter(BaseJWTTokenAdapter):
    
    @classmethod
    def encode_jwt(
        cls,
        payload: dict,
        key: str = settings.jwt_auth.jwt_private_path.read_text(),
        algorithm: str = settings.jwt_auth.algorithm,
        expire_minutes: int = settings.jwt_auth.expire_minutes,
        expire_timedelta: timedelta | None = None,
    ) -> str:
        to_encode = payload.copy()
        now = datetime.now(UTC)
        if expire_timedelta:
            expire = now + expire_timedelta
        else:
            expire = now + timedelta(minutes=expire_minutes)
        to_encode.update(
            {
                "exp": expire,
                "iat": now,
                "jti": str(uuid.uuid4()),
            }
        )
    
        return jwt.encode(to_encode, key, algorithm)
    
    @classmethod
    def decode_jwt(
        cls,
        token: str,
        key: str = settings.jwt_auth.jwt_public_path.read_text(),
        algoritms: list = [settings.jwt_auth.algorithm],
    ) -> dict:
        return jwt.decode(token, key, algoritms)