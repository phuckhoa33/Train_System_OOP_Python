from Interface.WagonInterface import Wagon
from Enum.WagonEnum import WagonType
from WagonManagmentSystem import HeadHeadManagementSystem, TailHeadManagementSystem, PassengerManagementSystem, RestaurantManagementSystem, CargoManagementSystem

class Head(Wagon):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.__type = WagonType.HEAD

    def display(self):
        return "HHHH"

class FirstHead(Head):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.update_system(HeadHeadManagementSystem(self.__code))

    def display(self):
        return "<" + super().display()

class LastHead(Head):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.update_system(TailHeadManagementSystem(self.__code))

    def display(self):
        return super().display() + ">"
    

class Passenger(Wagon):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.__type = WagonType.PASSENGER
        self.update_system(PassengerManagementSystem(self.__code))
    
    def display(self):
        return "|OOOO|"
class Restaurant(Wagon):
    def __init__(self, code: str, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.__type = WagonType.RESTAURANT
        self.update_system(RestaurantManagementSystem(self.__code))

    def display(self):
        return "|hThT|"

class Cargo(Wagon):
    def __init__(self, code: str, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.__type = WagonType.CARGO
        self.update_system(CargoManagementSystem(self.__code))

    def display(self):
        if self.__isFull:
            return "|____|"
        return "|^^^^|"