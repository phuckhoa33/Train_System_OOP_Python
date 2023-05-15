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

class AdminInterface(ABC):
    @abstractmethod
    def grant_rights(self):
        pass 

    @abstractmethod
    def create_new_chair(self, wagon_id):
        pass

    @abstractmethod
    def create_new_wagon(self, train_id: int):
        pass 

    @abstractmethod 
    def create_new_train(self):
        pass 