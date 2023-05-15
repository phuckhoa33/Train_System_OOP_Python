from Enum.GenderEnum import GenderState
from Enum.PersonEnum import PersonEnum
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass

class Co_Driver(PersonBaseClass):
    def __init__(self, email: str, fullname: str, code: int, telephoneNumber: str, gender: GenderState) -> None:
        super().__init__(email, fullname, code, telephoneNumber, gender)
        self.update_type(PersonEnum.CO_DRIVER)
