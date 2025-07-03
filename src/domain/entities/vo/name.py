from dataclasses import dataclass
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

@dataclass  # Removido frozen=True para permitir mutabilidade
class Name(Notifiable):
    first_name: str
    last_name: str

    def __post_init__(self):
        Notifiable.__init__(self)
        contract = (
            Contract()
            .requires(self.first_name, 'first_name')
            .requires(self.last_name, 'last_name')
            .is_greater_or_equals_than(self.first_name, 2, 'first_name')
            .is_greater_or_equals_than(self.last_name, 2, 'last_name')
            .is_lower_or_equals_than(self.first_name, 100, 'first_name')
            .is_lower_or_equals_than(self.last_name, 100, 'last_name')
        )
        self.add_notifications(contract.get_notifications())

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"