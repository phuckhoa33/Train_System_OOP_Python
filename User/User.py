from Enum.GenderEnum import GenderState
from Contact.PhoneNumber import PhoneNumber
from Interface.UserInterface import PersonInterface

class User(PersonInterface):
    def __init__(self, email: str, fullname: str, code: str, telephoneNumber: str, gender: GenderState) -> None:
        self.__email = email
        self.__fullname = fullname
        self.__code = code
        self.__telephoneNumber = PhoneNumber(telephoneNumber)
        self.__gender = gender

    def __cancel_ticket(self, code: int):
        pass 

    def _set_ticket(self):
        pass 

    def __payment(self):
        pass 