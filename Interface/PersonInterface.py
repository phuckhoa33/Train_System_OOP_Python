from abc import ABC, abstractmethod
from Contact.PhoneNumber import PhoneNumber
from Enum.GenderEnum import GenderState
from Enum.PersonEnum import PersonEnum

class Person(ABC):
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

class UserInterface(ABC):
    @abstractmethod
    def cancel_ticket(self, code: int):
        pass 

    @abstractmethod
    def set_ticket(self):
        pass 

    @abstractmethod
    def payment(self):
        pass 

class PersonManagementSystem(ABC):
    def __init__(self) -> None:
        pass 

    @abstractmethod
    def find(self):
        pass 

    @abstractmethod 
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass 