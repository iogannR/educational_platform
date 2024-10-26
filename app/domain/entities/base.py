from abc import ABC
from dataclasses import dataclass

from app.domain.value_objects.idvo import IdVO


@dataclass
class BaseEntity(ABC):
    id: IdVO