from Enum.ChairEnum import ChairType
from Interface.ChairInterface import ChairBaseClass

class HardChair(ChairBaseClass):
    def __init__(self, code: str, wagon_id: int, state: str) -> None:
        self.initiate_information(code, ChairType.HARD, wagon_id, state)

class SoftChair(ChairBaseClass):
    def __init__(self, code: str, wagon_id: int, state: str) -> None:
        self.initiate_information(code, ChairType.SOFT, wagon_id, state)

class Room(ChairBaseClass):
    def __init__(self, code: str, wagon_id: int, state: str) -> None:
        self.initiate_information(code, ChairType.ROOM, wagon_id, state)