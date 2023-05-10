from Enum.GenderEnum import GenderState
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass

class Waiter(PersonBaseClass):
    def __init__(self, email: str, fullname: str, code: str, telephoneNumber: str, gender: GenderState, train_code: str) -> None:
        super().__init__(email, fullname, code, telephoneNumber, gender)
        self.__train_code = train_code