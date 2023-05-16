from Enum.ChairEnum import ChairType
from GasStation.Train.Wagon.Chair.AbstractClass.ChairAbstractClass import ChairBaseClass
from Interface.DatabaseInterface import DatabaseConnection

class Room(ChairBaseClass):
    def __init__(self, code: int, wagon_id: int, state: str) -> None:
        self.initiate_information(code, ChairType.ROOM, wagon_id, state)