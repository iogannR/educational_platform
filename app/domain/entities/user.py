from dataclasses import dataclass

from app.domain.entities.base import BaseEntity


@dataclass
class UserEntity(BaseEntity):
    username: str
    email: str
    password: str