from dataclasses import dataclass, field
from uuid import UUID, uuid4

from src.domain.entities.vo.address import Address
from src.domain.entities.vo.name import Name

@dataclass(frozen=True)
class User:
    id: UUID = field(default_factory=uuid4, init=False)
    name: Name
    age: int
    address: Address
