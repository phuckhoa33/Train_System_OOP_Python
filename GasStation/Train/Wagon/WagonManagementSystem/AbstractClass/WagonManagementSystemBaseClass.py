from abc import ABC, abstractmethod
from configuration.Database import MysqlDatabaseConnection
from GasStation.Train.Wagon.Chair.HardChair import HardChair
from GasStation.Train.Wagon.Chair.SortChair import SoftChair
from GasStation.Train.Wagon.Chair.Room import Room
from GasStation.PersonObject.PersonManagementSystem import UserManagementSystem
from Interface.ChairInterface import ChairInterface
from Interface.PersonInterface import UserInterface
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
from Interface.DatabaseInterface import DatabaseConnection


class WagonManagementSystemBaseClass(ABC):
    def __init__(self, code: int, database: DatabaseConnection) -> None:
        self.code = code 
        self.database = database
        self.__user_manager = UserManagementSystem()
        self.__data = self.__get_data_depend_on_wagon_type()
        self.__chairs = self.__get_chairs()

    def admin_catalog(self, person: PersonBaseClass):
        choose: int = -1

        while choose != 0:
            print("-------------------------------------------------------\n"\
                "1. Find chair\n"\
                "2. Update chair\n"\
                "3. Create chair\n"\
                "0. Exit\n"\
                "---------------------------------------------------------\n")
            choose = int(input("What your chosen: "))

            match choose:
                case 1: 
                    a = int(input("What code: "))
                    self.__find_information_of_chair_room_goods(a)
                case 2: 
                    state = input("What state do you want to change: ")
                    converted_state = input("What state do you want to change into: ")
                    self.__convert_state_of_all_chair(state, converted_state)
                case 3: 
                    self.create_new_chair_or_room_or_insert_goods()
                case 0:
                    break 
    def user_catalog(self, person: PersonBaseClass):
        choose: int = -1

        while choose != 0:
            print("-------------------------------------------------------\n"\
                "1. Find chair\n"\
                "2. Buy chair\n"\
                "0. Exit\n"\
                "---------------------------------------------------------\n")
            choose = int(input("What your chosen: "))

            match choose:
                case 1: 
                    a = int(input("What code: "))
                    self.__find_information_of_chair_room_goods(a)
                case 2: 
                    self.__buy_ticket(person)
                case 0:
                    return

    def __get_all_available_chair(self):
        self.database.connect()
        query = f"SELECT chair_id, chair_type FROM chair WHERE state = 'unactive' and wagon_id = {self.code}"
        tickets = self.database.query_have_return(query)
        self.database.disconnect()
        return tickets

    def __buy_ticket(self, user: UserInterface):
        tickets = self.__get_all_available_chair()
        tks = [ticket['chair_id'] for ticket in tickets]

        if len(tickets) == 0:
            print("Tickets is over")
            return 

        print("------------------------------------")
        for ticket in tickets:
            print(f"Id: {ticket['chair_id']} and chair type: {ticket['chair_type']}")
        print("------------------------------------")
        choose = int(input("What ticket do you want to select: "))

        
        if choose in tks:
            print(self.__chairs)
            chair: ChairInterface = self.__chairs[choose]   
            chair.displayInformation()
            vertify = input("Do you want to pay this payment? ")

            if vertify=="yes":
                if user.payment():
                    print("Very happy to have served you. See you next time")
                else:
                    print("Please check your information so that pay this bill")
            else:
                print("See you again!!")
        else:
            print("See you again")
    
    def __get_chairs(self) -> list:
        D_chairs = {}
        for data in self.__data:
            chair = None 
            chair_id = int(data['chair_id'])
            wagon_id = int(data['wagon_id'])
            if data['chair_type']=='hard':
                chair = HardChair(chair_id, wagon_id, data['state'], self.database)
    
            elif data['chair_type']=='soft': 
                chair = SoftChair(chair_id, wagon_id, data['state'], self.database)
                
            elif data['chair_type']=='room':
                chair = Room(chair_id, wagon_id, data['state'], self.database)
                

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


    def __find_information_of_chair_room_goods(self, code: int):
        try:
            infor = self.__chairs[code].displayInformation()
            print(infor)
        except KeyError:
            print("Your chosen don't have in this wagon")
    
    def __convert_state_of_all_chair(self, state: str, current_state: str):
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