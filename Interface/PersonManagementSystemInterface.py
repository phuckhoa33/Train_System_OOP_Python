from abc import ABC, abstractmethod

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