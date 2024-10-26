import uuid

from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
)

from app.infrastructure.config import settings


class Base(DeclarativeBase):
    __abstract__ = True
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    
    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"