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

class PersonManagementSystem(ABC):
    def __init__(self) -> None:
        pass 

    @abstractmethod
    def find(self):
        pass 

    @abstractmethod 
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass 