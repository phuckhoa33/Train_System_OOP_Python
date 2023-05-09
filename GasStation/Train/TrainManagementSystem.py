from configuration.Database import MysqlDatabaseConnection
from GasStation.Train.Wagon.Wagon import FirstHead, LastHead, Passenger, Restaurant, Cargo
from AbstractClass.PersonAbstractClass import PersonBaseClass
from AbstractClass.WagonAbstractClass import WagonBaseClass
from Enum.PersonEnum import PersonEnum

class TrainManagementSystem():
    def __init__(self, code: int) -> None:
        self.__code = code 
        self.database = MysqlDatabaseConnection()

    @property
    def __data(self):
        self.database.connect()
        query = f"SELECT wagon_id, width, height, length, wagon_type FROM wagon WHERE train_id = {self.__code}"
        wagons = self.database.query_have_return(query)
        self.database.disconnect()
        return wagons

    @property
    def __wagons(self):

        D_wagon = {}
        for wagon in self.__data:
            checked_wagon = None 
            wagon_id = int(wagon['wagon_id'])
            width = int(wagon['width'])
            height = int(wagon['height'])
            length = int(wagon['length'])

            if wagon['wagon_type']=="firsthead":
                checked_wagon = FirstHead(wagon_id, width, height, length)
            elif wagon['wagon_type']=="tailhead":
                checked_wagon = LastHead(wagon_id, width, height, length)
            elif wagon['wagon_type']=="passenger":
                checked_wagon = Passenger(wagon_id, width, height, length)
            elif wagon['wagon_type']=="restaurant":
                checked_wagon = Restaurant(wagon_id, width, height,length)
            elif wagon['wagon_type']=="cargo":
                checked_wagon = Cargo(wagon_id, width, height, length)

            if checked_wagon == None:
                continue
            
            D_wagon[wagon_id] = checked_wagon
        return D_wagon

    def __create_wagon(self, wagon_type: str, width, height, length):
        self.database.connect()
        query = "INSERT INTO wagon(train_id, width, height, length, wagon_type) VALUES (%s, %s, %s, %s, %s)"
        val = (self.__code, width, height, length, wagon_type)
        self.database.query_have_not_return(query, val) 
        self.database.disconnect()

    def __find_wagon(self, code: int, person: PersonBaseClass):
        self.__wagons[code].display_catalog(person)

    def __display_train_running(self):
        sequence = "".join([wagon.display() for wagon in self.__wagons.values()])
        print(sequence)

    def catalog(self, person: PersonBaseClass):
        print(self.__wagons)
        choose = -1
        while choose != 0:
            print("----------------------------------")
            print("1. Find wagon")
            if person.type == PersonEnum.ADMIN:
                print("2. Create wagon")
            print("3. Display and watch train running") 
            print("0. Exit")
            print("----------------------------------")

            choose = int(input("Your chosen is: "))

            match choose:
                case 1: 
                    code = int(input("What code of wagon do you want to find: "))
                    wagon: WagonBaseClass = self.__find_wagon(code, person)
                    wagon.display_catalog()
                case 2:
                    if person.type == PersonEnum.USER:
                        continue
                    wagon_type = input("What wagon do you want to create: ")
                    if wagon_type not in ["restaurant", "cargo", "firsthead", "lasthead", "passenger"] :
                        print("Your chosen wagon type is invalid")
                        continue 
                    width = int(input("How many width: "))
                    height = int(input("How many height: "))
                    length = int(input("How many length: "))
                    self.__create_wagon(wagon_type, width, height, length)
                case 3: 
                    self.__display_train_running()
                case 0: 
                    print("Thank you for your concerns to us")
                    break 
                case _:
                    print("Your chosen is invalid")
