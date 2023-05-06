from abc import ABC, abstractmethod
from configuration.Database import MysqlDatabaseConnection
from GasStation.Train.Wagon.Chair import HardChair, SoftChair, Room
from GasStation.PersonObject.PersonManagementSystem import UserManagementSystem
from Interface.ChairInterface import ChairInterface
from Interface.PersonInterface import UserInterface
from AbstractClass.PersonAbstractClass import PersonBaseClass
from Enum.PersonEnum import PersonEnum

class WagonBaseClass(ABC):
    def __init__(self, code: int, width: int, height: int, length: int) -> None:
        self.code = code
        self.__width = width
        self.__height = height
        self.__length = length
        self.__manager = None

    def update_system(self, manager):
        self.__manager = manager
        self.__isFull = self.__manager.get_full_state()

    def display_catalog(self, person: PersonBaseClass):
        if person.type==PersonEnum.USER:
            self.__manager.buy_ticket()
        elif person.type==PersonEnum.ADMIN:
            self.__manager.admin_catalog()

    @abstractmethod
    def display(self):
        pass 


class WagonManagementSystemBaseClass(ABC):
    def __init__(self, code: int) -> None:
        self.code = code 
        self.database = MysqlDatabaseConnection()
        self.__user_manager = UserManagementSystem()
        self.__data = self.__get_data_depend_on_wagon_type()
        self.chairs = self.__get_chairs()

    def admin_catalog(self):
        choose: int = -1

        while choose != 0:
            print("-------------------------------------------------------\n"\
                "1. Find chair\n"\
                "2. Update chair\n"\
                "3. Create chair\n"\
                "0. Exit\n"\
                "---------------------------------------------------------\n")
            choose = input("What your choosen: ")

            match choose:
                case 1: 
                    a = int(input("What code: "))
                    self.find_information_of_chair_room_goods(a)
                case 2: 
                    state = input("What state do you want to change: ")
                    converted_state = input("What state do you want to change into: ")
                    self.convert_state_of_all_chair(state, converted_state)
                case 3: 
                    self.create_new_chair_or_room_or_insert_goods()
                case 0:
                    break 

    def buy_ticket(self, user: UserInterface):
        self.database.connect()
        query = "SELECT chair_id, chair_type FROM chair WHERE state = 'unactive'"
        tickets = self.database.query_have_return(query)
        tks = [ticket['chair_id'] for ticket in tickets]

        print("------------------------------------")
        for ticket in tickets:
            print(f"Id: {ticket['chair_id']} and chair type: {ticket['chair_type']}")
        print("------------------------------------")
        choose = int(input("What ticket do you want to select: "))

        
        if choose in tks:
            chair: ChairInterface = self.chairs[choose]   
            chair.displayInformation()
            vertify = input("Do you want to pay this payment? ")

            if vertify:
                if user.payment():
                    print("Very happy to have served you. See you next time")
                else:
                    print("Please check your information so that pay this bill")
            else:
                print("See you again!!")
        else:
            print("See you again")
        self.database.disconnect()
    
    def __get_chairs(self) -> list:
        D_chairs = {}
        for data in self.__data:
            chair = None 
            chair_id = int(data['chair_id'])
            wagon_id = int(data['wagon_id'])
            if data['chair_type']=='hard':
                chair = HardChair(chair_id, wagon_id, data['state'])
    
            elif data['chair_type']=='soft': 
                chair = SoftChair(chair_id, wagon_id, data['state'])
                
            elif data['chair_type']=='room':
                chair = Room(chair_id, wagon_id, data['state'])
                

            if data['user_id']!=0:
                user = self.__user_manager.mapping(int(data['user_id']))
                chair.set_ownership(user)
            
            D_chairs[int(data['chair_id'])] = chair

        return D_chairs

    def __get_data_depend_on_wagon_type(self) -> list:
        query = f"SELECT * FROM chair WHERE wagon_id = '{self.code}'"
        self.database.connect()
        a = self.database.query_have_return(query)
        self.database.disconnect()
        return a


    def find_information_of_chair_room_goods(self, code: int):
        infor = self.chairs[code].displayInformation()
        print(infor)

    def convert_state_of_all_chair(self, state: str, current_state: str):
        self.database.connect()
        query = f"UPDATE chair SET state = %s WHERE wagon_id = %s and state = %s"
        val = (state, self.code, current_state)
        self.database.query_have_not_return(query, val)
        self.database.disconnect()

    def get_full_state(self) -> bool:
        for data in self.__data:
            if data['state']=="unactive" or data['state']=="waiting":
                return False 
            
        return True 
        
    @abstractmethod
    def create_new_chair_or_room_or_insert_goods(self):
        pass 