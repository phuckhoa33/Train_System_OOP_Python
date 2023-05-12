from GasStation.Train.Wagon.WagonType.AbstractClass.WagonAbstractClass import WagonBaseClass
from Enum.WagonEnum import WagonType
from GasStation.Train.Wagon.WagonManagementSystem.PassengerWagonManagementSystem import PassengerManagementSystem
from Interface.DatabaseInterface import DatabaseConnection

class Passenger(WagonBaseClass):
    def __init__(self, code: int, width: int, height: int, length: int, database: DatabaseConnection) -> None:
        super().__init__(code, width, height, length)
        self.type = WagonType.PASSENGER
        self.update_system(PassengerManagementSystem(self.code, database))
    def display(self):
        return "::|OOOO|::"