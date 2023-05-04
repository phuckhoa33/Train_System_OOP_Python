from abc import ABC, abstractmethod
from Contact.PhoneNumber import PhoneNumber
from Enum.GenderEnum import GenderState
from Enum.PersonEnum import PersonEnum

class PersonBaseClass(ABC):
    def __init__(self, email: str, fullname: str, code: int, telephoneNumber: str, gender: GenderState) -> None:
        self.email = email
        self.fullname = fullname
        self.code = code
        self.telephoneNumber = PhoneNumber(telephoneNumber)
        self.gender = gender
        self.type = None

    def update_type(self, type: PersonEnum):
        self.type = type

    @abstractmethod
    def displayPersonInformation(self):
        pass