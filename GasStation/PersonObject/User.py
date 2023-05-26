from Enum.GenderEnum import GenderState
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
from Interface.PersonInterface import UserInterface
from Enum.PersonEnum import PersonEnum

class User(PersonBaseClass, UserInterface):
    def __init__(self, email: str, fullname: str, code: str, telephoneNumber: str, gender: GenderState) -> None:
        super().__init__(email, fullname, code, telephoneNumber, gender)
        self.update_type(PersonEnum.USER)

    def create_ticket(self):
        return super().create_ticket()

    def cancel_ticket(self, code: int):
        pass 

    def __payment(self):
        self.payment()
    
    def recharge(self):
        return super().recharge()
    
    