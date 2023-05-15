from Enum.GenderEnum import GenderState
from Enum.PersonEnum import PersonEnum
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass

class Driver(PersonBaseClass):
    def __init__(self, email: str, fullname: str, code: str, telephoneNumber: str, gender: GenderState, train_code: str) -> None:
        super().__init__(email, fullname, code, telephoneNumber, gender)
        self.update_type(PersonEnum.DRIVER)

    