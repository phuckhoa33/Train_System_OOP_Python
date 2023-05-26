from abc import ABC, abstractmethod
from GasStation.Train.Wagon.Chair.HardChair import HardChair
from GasStation.Train.Wagon.Chair.SortChair import SoftChair
from GasStation.Train.Wagon.Chair.Room import Room
from Interface.ChairInterface import ChairInterface
from Interface.PersonInterface import UserInterface, AdminInterface, PersonInterface
from Interface.DatabaseInterface import DatabaseConnection
from GasStation.PersonObject.PersonManagementSystem import UserManagementSystem
from caching.GlobalStorage import global_storage
from Enum.PersonEnum import PersonEnum


class WagonManagementSystemBaseClass(ABC):
    def __init__(self, code: int) -> None:
        self.code = code 
        self.database: DatabaseConnection = global_storage.get('database')
        self.__person: PersonInterface = global_storage.get("person")
    """
        This part so that create properties with connect with database.
        Note: This part is similiar with another property
    """

    @property
    def __chairs(self) -> list:
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
                user = self.__manager.mapping(int(data['user_id']))
                chair.set_ownership(user)
            
            D_chairs[int(data['chair_id'])] = chair

        return D_chairs

    @property
    def __data(self) -> list:
        query = f"SELECT * FROM chair WHERE wagon_id = '{self.code}'"
        self.database.connect()
        a = self.database.query_have_return(query)
        self.database.disconnect()
        return a

    def __get_all_available_chair(self):
        self.database.connect()
        query = f"SELECT chair_id, chair_type FROM chair WHERE state = 'unactive' and wagon_id = {self.code}"
        tickets = self.database.query_have_return(query)
        self.database.disconnect()
        return tickets

    def __buy_ticket(self):
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
                if self.__user.payment():
                    print("Very happy to have served you. See you next time")
                else:
                    print("Please check your information so that pay this bill")
            else:
                print("See you again!!")
        else:
            print("See you again")
    


    def __find_information_of_chair_room_goods(self, code: int):
        try:
            code = int(input("What code: "))
            chair: ChairInterface = self.__chairs[code]
            infor = chair.displayInformation()
            print(infor)
        except KeyError:
            print("Your chosen don't have in this wagon")
    
    def __convert_state_of_all_chair(self, state: str, current_state: str):
        state = input("What state do you want to change: ")
        converted_state = input("What state do you want to change into: ")
        self.database.connect()
        query = f"UPDATE chair SET state = %s WHERE wagon_id = %s and state = %s"
        val = (converted_state, self.code, state)
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