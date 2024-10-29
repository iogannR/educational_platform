from __future__ import annotations

from uuid import UUID
from dataclasses import asdict

from pydantic import BaseModel

from app.domain.entities.user import UserEntity


class UserCreate(BaseModel):
    id: UUID
    username: str
    email: str
    password: str
    
    def to_entity(self) -> UserEntity:
        entity = UserEntity(
            id=self.id,
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