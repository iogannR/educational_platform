from __future__ import annotations

from dataclasses import asdict

from pydantic import BaseModel

from app.domain.entities.user import UserEntity
from app.domain.value_objects.idvo import IdVO


class UserResponse(BaseModel):
    id: IdVO
    username: str
    email: str
    
    @classmethod
    def from_entity(cls, entity: UserEntity) -> UserResponse:
        return cls(**asdict(entity))