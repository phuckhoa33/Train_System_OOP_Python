from abc import ABC, abstractmethod
from GasStation.Train.Wagon.WagonManagementSystem.AbstractClass.WagonManagementSystemBaseClass import WagonManagementSystemBaseClass

class WagonBaseClass(ABC):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        self.code = code
        self.__width = width
        self.__height = height
        self.__length = length
        self.__manager: WagonManagementSystemBaseClass = None

    def update_system(self, manager):
        self.__manager = manager
        self.isFull = self.__manager.get_full_state()

    def display_catalog(self):
        self.__manager.catalog()

    @abstractmethod
    def display(self):
        print(f"The train code is {self.code}\
              Width's train is {self.__width}\
              Height's train is {self.__height}\
              Length's train is {self.__length}")