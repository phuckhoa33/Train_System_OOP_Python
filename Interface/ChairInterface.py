from abc import ABC, abstractmethod
from Interface.PersonInterface import UserInterface
from Enum.ChairEnum import ChairType, ChairState

class ChairInterface(ABC):
    @abstractmethod
    def initiate_information(self, __code: str, type: ChairType, wagon_id: str, state: str):
        pass 

    @abstractmethod
    def set_ownership(self, owner: UserInterface) -> None:
        pass 

    @abstractmethod
    def update_state(self, state: ChairState) -> None:
        pass 

    @abstractmethod
    def update_type(self, type: ChairType) -> None:
        pass 

    @abstractmethod
    def displayInformation(self):
        pass 