from Enum.ChairEnum import ChairType
from GasStation.Train.Wagon.Chair.AbstractClass.ChairAbstractClass import ChairBaseClass

class SoftChair(ChairBaseClass):
    def __init__(self, code: int, wagon_id: int, state: str) -> None:
        self.initiate_information(code, ChairType.SOFT, wagon_id, state)