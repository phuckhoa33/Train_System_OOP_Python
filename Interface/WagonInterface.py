from abc import ABC, abstractmethod
from Enum.WagonEnum import WagonType

class Wagon(ABC):
    def __init__(self, code: str, width: int, height: int, length: int) -> None:
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
        self.__code = code 

    @abstractmethod
    def get_data_depend_on_wagon_type(self, type: WagonType):
        pass 