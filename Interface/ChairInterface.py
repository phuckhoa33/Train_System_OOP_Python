from Enum.ChairEnum import ChairState, ChairType
from Interface.PersonInterface import Person
from configuration.Database import MysqlDatabaseConnection
from abc import ABC, abstractmethod

class ChairInterface(ABC):
    @abstractmethod
    def initiate_information(self, __code: str, type: ChairType, wagon_id: str, state: str):
        pass 

    @abstractmethod
    def set_ownership(self, owner: Person) -> None:
        pass 

    @abstractmethod
    def __update_state(self, state: ChairState) -> None:
        pass 

    @abstractmethod
    def __update_type(self, type: ChairType) -> None:
        pass 

    @abstractmethod
    def displayInformation(self):
        pass 


class ChairBaseClass(ChairInterface):
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
        query = f"UPDATE chair SET user_id = %s WHERE chair_id = %s"
        val = (owner.code, self.__code)
        self.__database.connect()
        self.__database.query_have_not_return(query, val)
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
