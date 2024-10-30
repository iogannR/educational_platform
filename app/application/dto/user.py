from __future__ import annotations

from uuid import UUID, uuid4
from dataclasses import asdict

from pydantic import BaseModel, Field

from app.domain.entities.user import UserEntity


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    
    def to_entity(self) -> UserEntity:
        entity = UserEntity(
            username=self.username,
            email=self.email,
            password=self.password,
        )

        return entity
    

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str
    
    @classmethod
    def from_entity(cls, entity: UserEntity) -> UserResponse:
        return cls(**asdict(entity))