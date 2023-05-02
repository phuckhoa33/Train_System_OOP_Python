from abc import ABC, abstractmethod
from Enum.WagonEnum import WagonType
from configuration.Database import MysqlDatabaseConnection
from GasStation.Train.Wagon.Chair import HardChair, SoftChair, Room

from GasStation.PersonObject.PersonManagementSystem import UserManagementSystem
class Wagon(ABC):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        self.__code = code 
        self.__width = width
        self.__height = height
        self.__length = length
        self.__isFull = False

    @abstractmethod
    def display(self):
        pass 

class WagonManagementSystem(ABC):
    def __init__(self, code: int) -> None:
        self.__code = code 
        self.__database = MysqlDatabaseConnection()
        self.__user_manager = UserManagementSystem()
        self.__data = self.__get_data_depend_on_wagon_type()
    
    @property
    def _chairs(self):
        L_chair = []
        for data in self.__data:
            chair = None 
            if data['chair_type']=='hard':
                chair = HardChair(data['chair_id'], data['wagon_id'], data['state'])
    
            elif data['chair_type']=='soft':
                chair = SoftChair(data['chair_id'], data['wagon_id'], data['state'])
                
            elif data['chair_type']=='room':
                chair = Room(data['chair_id'], data['wagon_id'], data['state'])
                

            if data['user_id']!=0:
                user = self.__user_manager.mapping(int(data['user_id']))
                chair.set_ownership(user)

            L_chair.append(chair)

            return L_chair

    def __get_data_depend_on_wagon_type(self) -> list:
        query = f"SELECT * FROM chair WHERE wagon_id = '{self.__code}'"
        self.__database.connect()
        a = self.__database.query_have_return(query)
        print(a)
        return a


    @abstractmethod
    def find_information_of_chair_room_goods(self, code: int):
        pass 

    @abstractmethod
    def create_new_chair_or_room_or_insert_goods(self, code: int):
        pass 

    @abstractmethod
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 