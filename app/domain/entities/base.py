from abc import ABC
from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class BaseEntity(ABC):
    id: UUID = field(default_factory=uuid4)