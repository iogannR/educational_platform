import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True)
class IdVO:
    value: uuid.UUID = field(default_factory=uuid.uuid4)