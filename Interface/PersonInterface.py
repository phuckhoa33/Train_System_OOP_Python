from abc import ABC, abstractmethod
from Contact.PhoneNumber import PhoneNumber
from Enum.GenderEnum import GenderState

class Person(ABC):
    def __init__(self, email: str, fullname: str, code: str, telephoneNumber: str, gender: GenderState) -> None:
        self.__email = email
        self.__fullname = fullname
        self.__code = code
        self.__telephoneNumber = PhoneNumber(telephoneNumber)
        self.__gender = gender

    @abstractmethod
    def displayPersonInformation(self):
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