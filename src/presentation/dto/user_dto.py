from dataclasses import dataclass

from flask import jsonify

from src.domain.entities.user import User

@dataclass
class CreateUserDTO:
    first_name: str
    last_name: str
    age: int
    street: str
    number: str
    complement: str
    district: str
    city: str
    state: str
    zip_code: str
    country: str

    @staticmethod
    def from_dict(data: dict) -> 'CreateUserDTO':
        return CreateUserDTO(
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            age=data.get('age', 0),
            street=data.get('street', ''),
            number=data.get('number', ''),
            complement=data.get('complement', ''),
            district=data.get('district', ''),
            city=data.get('city', ''),
            state=data.get('state', ''),
            zip_code=data.get('zip_code', ''),
            country=data.get('country', '')
        )

    @staticmethod
    def to_json(user: User):
        return jsonify({
            'id': str(user.id),
            'name': user.name.full_name,
            'age': user.age,
            'address': {
                'street': user.address.street,
                'number': user.address.number,
                'complement': user.address.complement,
                'district': user.address.district,
                'city': user.address.city,
                'state': user.address.state,
                'zip_code': user.address.zip_code,
                'country': user.address.country
            }
        }), 201