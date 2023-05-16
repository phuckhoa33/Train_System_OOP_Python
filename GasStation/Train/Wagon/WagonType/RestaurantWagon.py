from GasStation.Train.Wagon.WagonType.AbstractClass.WagonAbstractClass import WagonBaseClass
from Enum.WagonEnum import WagonType
from GasStation.Train.Wagon.WagonManagementSystem.RestaurantWagonManagementSystem import RestaurantManagementSystem
from Interface.DatabaseInterface import DatabaseConnection

class Restaurant(WagonBaseClass):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.type = WagonType.RESTAURANT
        self.update_system(RestaurantManagementSystem(self.code))

    def display(self):
        return "::|hThT|::"