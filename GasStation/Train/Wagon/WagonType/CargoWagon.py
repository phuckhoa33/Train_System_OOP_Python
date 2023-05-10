from GasStation.Train.Wagon.WagonType.AbstractClass.WagonAbstractClass import WagonBaseClass
from Enum.WagonEnum import WagonType
from GasStation.Train.Wagon.WagonManagementSystem.CargoWagonManagementSystem import CargoManagementSystem



class Cargo(WagonBaseClass):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        super().__init__(code, width, height, length)
        self.type = WagonType.CARGO
        self.update_system(CargoManagementSystem(self.code))

    def display(self):
        wagon = None
        if self.isFull:
            wagon = "|____|"
        else: 
            wagon = "|^^^^|"
        return "::" + wagon + "::"