from abc import ABC, abstractmethod


class PersonInterface(ABC):
    @abstractmethod
    def watch_train(self, train_id: int):
        pass 

    @abstractmethod
    def find(self, code: int, type: str):
        pass 

    @abstractmethod
    def displayPersonInformation(self):
        pass 

class UserInterface(ABC):
    @abstractmethod
    def cancel_ticket(self, code: int):
        pass 

    @abstractmethod
    def create_ticket(self):
        pass 

    @abstractmethod
    def recharge(self):
        pass 

    @abstractmethod
    def payment(self):
        pass 

    @abstractmethod
    def find(self):
        pass 


class PartAdministratorInterface(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod 
    def delete(self):
        pass 

    @abstractmethod
    def update(self):
        pass 

