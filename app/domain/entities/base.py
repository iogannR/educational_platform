from abc import ABC
from dataclasses import dataclass
from uuid import UUID


@dataclass
class BaseEntity(ABC):
    id: UUID