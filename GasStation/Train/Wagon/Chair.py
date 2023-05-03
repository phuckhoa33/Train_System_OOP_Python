from Enum.ChairEnum import ChairState, ChairType
from Interface.PersonInterface import Person
from configuration.Database import MysqlDatabaseConnection

class Chair():
    def __init__(self) -> None:
        raise NotImplementedError("Cannot instantiate this class")
    
    def initiate_information(self, __code: str, type: ChairType, wagon_id: str, state: str):
        self.__code = __code 
        self.__wagon_id = wagon_id
        self.__owner = None
        self.__state = state
        self.__database = MysqlDatabaseConnection()
        self.__update_type(type)

    def set_ownership(self, owner: Person) -> None:
        query = f"UPDATE user SET user_id = {owner.code} WHERE chair_id = {self.__code}"
        self.__database.query_have_not_return(query)
        self.__owner = owner
        self.__update_state(ChairState.ACTIVE)

    def __update_state(self, state: ChairState) -> None:
        self.__state = state

    def __update_type(self, type: ChairType) -> None:
        self.__type = type
    
    def displayInformation(self):
        return f"{'Empty ownership' if self.__owner == None else self.__owner.displayPersonInformation()}\n" \
                "Chair Information: \n"\
                f"Wagon: {self.__wagon_id}\nChairType: {self.__type}\nChairCode: {self.__code}\nState: {self.__state}\n" \
                "--------------------------------------------------------------------------------------"

class HardChair(Chair):
    def __init__(self, code: str, wagon_id: int, state: str) -> None:
        self.initiate_information(code, ChairType.HARD, wagon_id, state)

class SoftChair(Chair):
    def __init__(self, code: str, wagon_id: int, state: str) -> None:
        self.initiate_information(code, ChairType.SOFT, wagon_id, state)

class Room(Chair):
    def __init__(self, code: str, wagon_id: int, state: str) -> None:
        self.initiate_information(code, ChairType.ROOM, wagon_id, state)
