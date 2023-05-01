from Enum.ChairEnum import ChairState, ChairType
from Interface.PersonInterface import Person

class Chair():
    def __init__(self) -> None:
        raise NotImplementedError("Cannot instantiate this class")
    
    def initiate_information(self, __code: str, type: ChairType, wagon_id: str):
        self.__code = __code 
        self.__wagon_id = wagon_id
        self.__owner = None
        self.__state = None 
        self.__update_type(type)

    def set_ownership(self, owner: Person) -> None:
        self.__owner = owner
        self.__update_state(ChairState.ACTIVE)

    def __update_state(self, state: ChairState) -> None:
        self.__state = state

    def __update_type(self, type: ChairType) -> None:
        self.__type = type
    
    def displayInformation(self):
        return f"{'Empty ownership' if self.__owner == None else self.__owner.displayUserInformation()}\n" \
                "Chair Information: \n"\
                f"Wagon: {self.__wagon_id}\nChairType: {self.__type}\nChairCode: {self.__code}\nState: {self.__state}"

class HardChair(Chair):
    def __init__(self, code: str) -> None:
        self.initiate_information(code, ChairType.HARD)

class SoftChair(Chair):
    def __init__(self, code: str) -> None:
        self.initiate_information(code, ChairType.SOFT)

class Room(Chair):
    def __init__(self, code: str) -> None:
        self.initiate_information(code, ChairType.ROOM)