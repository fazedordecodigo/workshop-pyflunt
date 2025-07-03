from dataclasses import dataclass

@dataclass(frozen=True)
class Address:
    street: str
    number: str
    complement: str
    district: str
    city: str
    state: str
    zip_code: str
    country: str