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
        self.code = code 
        self.database = MysqlDatabaseConnection()
        self.__user_manager = UserManagementSystem()
        self.__data = self.__get_data_depend_on_wagon_type()
        self.chairs = self.__get_chairs()
    
    def __get_chairs(self) -> list:
        D_chairs = {}
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
            
            D_chairs[int(data['chair_id'])] = chair

        return D_chairs

    def __get_data_depend_on_wagon_type(self) -> list:
        query = f"SELECT * FROM chair WHERE wagon_id = '{self.code}'"
        self.__database.connect()
        a = self.__database.query_have_return(query)
        return a


    def find_information_of_chair_room_goods(self, code: int):
        infor = self.chairs[code].displayInformation()
        print(infor)

    @abstractmethod
    def create_new_chair_or_room_or_insert_goods(self):
        pass 

    @abstractmethod
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 