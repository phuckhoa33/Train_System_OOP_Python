from Contact.PhoneNumber import PhoneNumber
from Enum.GenderEnum import GenderState
from Enum.PersonEnum import PersonEnum
from Interface.PersonInterface import PersonInterface

class PersonBaseClass(PersonInterface):
    def __init__(self, email: str, fullname: str, code: int, telephoneNumber: str, gender: GenderState) -> None:
        self.email = email
        self.fullname = fullname
        self.code = code
        self.telephoneNumber = PhoneNumber(telephoneNumber)
        self.gender = gender
        self.type = None

    def update_type(self, type: PersonEnum):
        self.type = type

    def displayPersonInformation(self):
        return  "--------------------------------------------------------------------------------\n"\
                f"User Information\n" \
                f"Fullname: {self.fullname}\nEmail: {self.email} \n" \
                f"Telephone: {self.telephoneNumber.phone_number} \nUserCode: {self.code}\n" \
                f"Gender: {self.gender} \nTrainCode: {self.code}\n"\
                "--------------------------------------------------------------------------------\n"