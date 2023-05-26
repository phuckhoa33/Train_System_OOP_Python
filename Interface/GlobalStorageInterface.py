from abc import ABC, abstractmethod

class GlobalStorageInterface(ABC):

    @abstractmethod
    def add(self, attribute: object, name: str):
        pass 

    @abstractmethod 
    def remove(self, attribute: object, name: str):
        pass 

    @abstractmethod
    def update(self, attribute: object, name: str):
        pass 

    @abstractmethod
    def get(self, attribute: str) -> object:
        pass 