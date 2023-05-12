from GasStation.Train.Wagon.WagonType.AbstractClass.WagonAbstractClass import WagonBaseClass
from Enum.WagonEnum import WagonType
from GasStation.Train.Wagon.WagonManagementSystem.HeadWagonManagementSystem import HeadHeadManagementSystem, TailHeadManagementSystem
from Interface.DatabaseInterface import DatabaseConnection

class Head(WagonBaseClass):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)

    def display(self):
        return "HHHH"

class FirstHead(Head):
    def __init__(self, code: int, width: int, height: int, length: int, database: DatabaseConnection) -> None:
        super().__init__(code, width, height, length)
        self.type = WagonType.FIRST_HEAD
        self.update_system(HeadHeadManagementSystem(self.code, database))

    def display(self):
        return "<" + super().display() + "::"

class LastHead(Head):
    def __init__(self, code: int, width: int, height: int, length: int, database: DatabaseConnection) -> None:
        super().__init__(code, width, height, length)
        self.type = WagonType.LAST_HEAD
        self.update_system(TailHeadManagementSystem(self.code, database))

    def display(self):
        return "::"+super().display() + ">"