from Enum.GenderEnum import GenderState
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
from Enum.PersonEnum import PersonEnum


class Admin(PersonBaseClass):
    def __init__(self, email: str, fullname: str, code: int, telephoneNumber: str, gender: GenderState) -> None:
        super().__init__(email, fullname, code, telephoneNumber, gender)
        self.update_type(PersonEnum.ADMIN)