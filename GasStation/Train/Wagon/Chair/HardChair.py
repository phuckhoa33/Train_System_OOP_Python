from Enum.ChairEnum import ChairType
from GasStation.Train.Wagon.Chair.AbstractClass.ChairAbstractClass import ChairBaseClass

class HardChair(ChairBaseClass):
    def __init__(self, code: int, wagon_id: int, state: str) -> None:
        self.initiate_information(code, ChairType.HARD, wagon_id, state)