import re 

class PhoneNumber():
<<<<<<< HEAD
    def __init__(self, phone_number: str) -> None:
        if self.is_valid_vietnamese_phone_number(phone_number):
            self.phone_number = phone_number
        else: 
            raise ValueError("Invalid vietnamese phone number")
        
    def is_valid_vietnamese_phone_number(self, phone_number: str):
=======
    def __init__(self, phone_number: int) -> None:
        if self.is_valid_vietnamese_phone_number(phone_number):
            self.__phone_number = phone_number
        else: 
            raise ValueError("Invalid vietnamese phone number")
        
    def is_valid_vietnamese_phone_number(self):
>>>>>>> origin/wagon-and-train-branch
        """
        Check if the phone number is in the correct format for Vietnamese phone numbers
        """
        # Regular expression for the format of Vietnamese phone numbers
        regex = r"^\+84\d{9}$|^0\d{9}$|^84\d{9}$"

<<<<<<< HEAD
        if not re.match(regex, phone_number):
=======
        if not re.match(regex, self.telephoneNumber):
>>>>>>> origin/wagon-and-train-branch
            return False
        else:
            return True