from src.domain.entities.user import User
from src.domain.entities.vo.name import Name
from src.domain.entities.vo.address import Address
from src.infrastructure.logger import get_logger
from src.presentation.dto.user_dto import CreateUserDTO
from flunt.notifications.notification import Notification

class UserService:    
    @staticmethod
    def create_user(user: CreateUserDTO) -> User | list[Notification]:
        logger = get_logger()
        logger.info("Criando usuário...")
        if user.age < 0:
            logger.warning("Idade deve ser positiva.")
            raise ValueError("Idade deve ser positiva.")
        if not user.street or not user.city or not user.state or not user.zip_code or not user.country:
            logger.warning("Endereço incompleto.")
            raise ValueError("Endereço incompleto.")

        name = Name(first_name=user.first_name, last_name=user.last_name)
        address = Address(
            street=user.street,
            number=user.number,
            complement=user.complement,
            district=user.district,
            city=user.city,
            state=user.state,
            zip_code=user.zip_code,
            country=user.country
        )
        logger.info("Usuário criado com sucesso.")
        new_user = User(name=name, age=user.age, address=address)
        if not new_user.name.is_valid:
            logger.warning("Nome inválido.")
            return new_user.name.get_notifications()
        return new_user
