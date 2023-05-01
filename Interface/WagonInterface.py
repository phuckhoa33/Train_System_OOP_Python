from abc import ABC, abstractmethod
from Enum.WagonEnum import WagonType

class Wagon(ABC):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        self.__code = code 
        self.__width = width
        self.__height = height
        self.__length = length
        self.__isFull = False

    @abstractmethod
    def display(self):
        pass 

class WagonManagementSystem(ABC):
    def __init__(self, code: str) -> None:
        """
            This code is code of managing wagon.
            With below code is code of chair or room or position of cargo wagon
        """
        self.__code = code 

    @abstractmethod
    def get_data_depend_on_wagon_type(self, type: WagonType):
        pass 

    @abstractmethod
    def find_information_of_chair_room_goods(self, code: int):
        pass 

    @abstractmethod
    def create_new_chair_or_room_or_insert_goods(self, code: int):
        pass 

    @abstractmethod
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 