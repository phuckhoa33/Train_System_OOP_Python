from Enum.ChairEnum import ChairState, ChairType
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
from configuration.Database import MysqlDatabaseConnection
from Interface.ChairInterface import ChairInterface
from Interface.DatabaseInterface import DatabaseConnection



class ChairBaseClass(ChairInterface):
    def __init__(self) -> None:
        raise NotImplementedError("Cannot instantiate this class")
    
    def initiate_information(self, __code: str, type: ChairType, wagon_id: str, state: str, database: DatabaseConnection):
        self.__code = __code 
        self.__wagon_id = wagon_id
        self.__owner = None
        self.__state = state
        self.__database = database
        self.update_type(type)

    def set_ownership(self, owner: PersonBaseClass) -> None:
        query = f"UPDATE chair SET user_id = %s WHERE chair_id = %s"
        val = (owner.code, self.__code)
        self.__database.connect()
        self.__database.query_have_not_return(query, val)
        self.__owner = owner
        self.update_state(ChairState.ACTIVE)

    def update_state(self, state: ChairState) -> None:
        self.__state = state

    def update_type(self, type: ChairType) -> None:
        self.__type = type
    
    def displayInformation(self):
        return f"{'Empty ownership' if self.__owner == None else self.__owner.displayPersonInformation()}\n" \
                "Chair Information: \n"\
                f"Wagon: {self.__wagon_id}\nChairType: {self.__type}\nChairCode: {self.__code}\nState: {self.__state}\n" \
                "--------------------------------------------------------------------------------------"
