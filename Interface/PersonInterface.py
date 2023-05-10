from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def cancel_ticket(self, code: int):
        pass 

    @abstractmethod
    def set_ticket(self):
        pass 

    @abstractmethod
    def payment(self):
        pass 