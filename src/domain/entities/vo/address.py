from dataclasses import dataclass
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

@dataclass
class Address(Notifiable):
    street: str
    number: str
    complement: str
    district: str
    city: str
    state: str
    zip_code: str
    country: str

    def __post_init__(self):
        Notifiable.__init__(self)
        contract = (
            Contract()
            .requires(self.street, 'street')
            .requires(self.number, 'number')
            .requires(self.complement, 'complement')
            .requires(self.district, 'district')
            .requires(self.city, 'city')
            .requires(self.state, 'state')
            .requires(self.zip_code, 'zip_code')
            .requires(self.country, 'country')
            .is_lower_or_equals_than(self.street, 5, 'street')
            .is_lower_or_equals_than(self.number, 1, 'number')
            .is_lower_or_equals_than(self.complement, 100, 'complement')
            .is_lower_or_equals_than(self.district, 100, 'district')
            .is_lower_or_equals_than(self.city, 100, 'city')
            .is_lower_or_equals_than(self.state, 100, 'state')
            .is_lower_or_equals_than(self.zip_code, 10, 'zip_code')
            .is_lower_or_equals_than(self.country, 100, 'country')
        )
        self.add_notifications(contract.get_notifications())