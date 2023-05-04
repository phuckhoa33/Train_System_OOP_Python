from Enum.GenderEnum import GenderState
from AbstractClass.PersonAbstractClass import PersonBaseClass
from Interface.PersonInterface import UserInterface
from Enum.PersonEnum import PersonEnum

class User(PersonBaseClass, UserInterface):
    def __init__(self, email: str, fullname: str, code: str, telephoneNumber: str, gender: GenderState) -> None:
        super().__init__(email, fullname, code, telephoneNumber, gender)
        self.update_type(PersonEnum.USER)

    def cancel_ticket(self, code: int):
        pass 

    def set_ticket(self):
        pass 

    def payment(self):
        pass 

    def displayPersonInformation(self):
        return  "--------------------------------------------------------------------------------\n"\
                f"User Information\n" \
                f"Fullname: {self.fullname}\nEmail: {self.email} \n" \
                f"Telephone: {self.telephoneNumber.phone_number} \nUserCode: {self.code}\n" \
                f"Gender: {self.gender} \nTrainCode: {self.code}\n"\
                "--------------------------------------------------------------------------------"
    
    