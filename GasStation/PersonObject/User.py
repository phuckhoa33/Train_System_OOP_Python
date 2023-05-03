from Enum.GenderEnum import GenderState
from Contact.PhoneNumber import PhoneNumber
from Interface.PersonInterface import Person

class User(Person):
    def __init__(self, email: str, fullname: str, code: str, telephoneNumber: str, gender: GenderState) -> None:
        super().__init__(email, fullname, code, telephoneNumber, gender)

    def __cancel_ticket(self, code: int):
        pass 

    def __set_ticket(self):
        pass 

    def __payment(self):
        pass 

    def displayPersonInformation(self):
        return  "--------------------------------------------------------------------------------\n"\
                f"User Information\n" \
                f"Fullname: {self.fullname}\nEmail: {self.email} \n" \
                f"Telephone: {self.telephoneNumber.phone_number} \nUserCode: {self.code}\n" \
                f"Gender: {self.gender} \nTrainCode: {self.code}\n"\
                "--------------------------------------------------------------------------------"
    
    