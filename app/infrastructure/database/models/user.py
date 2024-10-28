from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.entities.user import UserEntity
from app.infrastructure.database.models.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(60), nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str]
    
    def to_entity(self) -> UserEntity:
        entity: UserEntity = UserEntity(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
        )
        return entity