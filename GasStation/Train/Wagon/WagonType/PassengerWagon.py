from GasStation.Train.Wagon.WagonType.AbstractClass.WagonAbstractClass import WagonBaseClass
from Enum.WagonEnum import WagonType
from GasStation.Train.Wagon.WagonManagementSystem.PassengerWagonManagementSystem import PassengerManagementSystem

class Passenger(WagonBaseClass):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.type = WagonType.PASSENGER
        self.update_system(PassengerManagementSystem(self.code))
    def display(self):
        return "::|OOOO|::"