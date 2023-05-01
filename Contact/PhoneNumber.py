import re 

class PhoneNumber():
    def __init__(self, phone_number: int) -> None:
        if self.is_valid_vietnamese_phone_number(phone_number):
            self.phone_number = phone_number
        else: 
            raise ValueError("Invalid vietnamese phone number")
        
    def is_valid_vietnamese_phone_number(self, phone_number: str):
        """
        Check if the phone number is in the correct format for Vietnamese phone numbers
        """
        # Regular expression for the format of Vietnamese phone numbers
        regex = r"^\+84\d{9}$|^0\d{9}$|^84\d{9}$"
        if not re.match(regex, phone_number):
            return False
        else:
            return True