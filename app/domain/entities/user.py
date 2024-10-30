from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity


@dataclass
class UserEntity(BaseEntity):
    username: str = field(default=None)
    email: str = field(default=None)
    password: str = field(default=None)