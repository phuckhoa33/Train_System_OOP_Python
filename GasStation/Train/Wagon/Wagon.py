from AbstractClass.WagonAbstractClass import WagonBaseClass
from Enum.WagonEnum import WagonType
from GasStation.Train.Wagon.WagonManagementSystem import HeadHeadManagementSystem, TailHeadManagementSystem, PassengerManagementSystem, RestaurantManagementSystem, CargoManagementSystem

class Head(WagonBaseClass):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.__type = WagonType.HEAD

    def display(self):
        return "HHHH"

class FirstHead(Head):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.update_system(HeadHeadManagementSystem(self.code))

    def display(self):
        return "<" + super().display() + "::"

class LastHead(Head):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.update_system(TailHeadManagementSystem(self.code))

    def display(self):
        return "::"+super().display() + ">"
    

class Passenger(WagonBaseClass):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.__type = WagonType.PASSENGER
        self.update_system(PassengerManagementSystem(self.code))
    
    def display(self):
        return "::|OOOO|::"
class Restaurant(WagonBaseClass):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.__type = WagonType.RESTAURANT
        self.update_system(RestaurantManagementSystem(self.code))

    def display(self):
        return "::|hThT|::"

class Cargo(WagonBaseClass):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.__type = WagonType.CARGO
        self.update_system(CargoManagementSystem(self.code))

    def display(self):
        wagon = None
        if self.__isFull:
            wagon = "|____|"
        else: 
            wagon = "|^^^^|"
        return "::" + wagon + "::"