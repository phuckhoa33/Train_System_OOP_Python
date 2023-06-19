from Interface.PersonInterface import PartAdministratorInterface, UserInterface
from caching.GlobalStorage import global_storage
from GasStation.PersonObject.Administrator.ChairAdministrator import ChairAdministrator
from GasStation.PersonObject.Administrator.TrainAdministrator import TrainAdministrator
from GasStation.PersonObject.Administrator.WagonAdministrator import WagonAdministrator
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
from Enum.PersonEnum import PersonEnum

class Catalog():

    def __init__(self) -> None:
        self.__person: PersonBaseClass = global_storage('person')

    def catalog(self):
        if self.__person.type==PersonEnum:
            self.__user: UserInterface = self.__person
            del self.__person
        else:
            self.__admin: PartAdministratorInterface = self.__person
            del self.__person

    def __user(self, part: str):
        while True:
            print("-------------------------------------")
            print(
                f"\nThis is user catalog of {part} part\n \
                    1. Find \n \
                    2. Buy \n\
                    3. Recharge\n\
                    4. Display train\n\
                    0. Cancle\n"
            )
            print("-------------------------------------\n")
            choose = int(input("Your chosen is: "))
            match choose:
                case 1:
                    self.__admin.find()
                case 2:
                    self.__admin.create()
                case 3:
                    self.__admin.update()
                case 4:
                    self.__admin.delete()
                case _:
                    break

    def __admin(self, part: str):
        while True:
            print("-------------------------------------")
            print(
                f"\nThis is admin catalog of {part} part\n\
                    1. Find\n\
                    2. Create\n\
                    3. Update\n\
                    4. Display train\n\
                    0. Delete\n"
            )
            print("-------------------------------------\n")
            choose = int(input("Your chosen is: "))
            match choose:
                case 1:
                    self.__admin.find()
                case 2:
                    self.__choose_admin_type()
                    self.__admin.create()
                case 3:
                    self.__choose_admin_type()
                    self.__admin.update()
                case 4:
                    self.__choose_admin_type()
                    self.__admin.delete()
                case _:
                    break
    def __choose_admin_type(self, choose):
        if choose=="train":
            self.__admin = TrainAdministrator()
        elif choose=="wagon":
            self.__admin = WagonAdministrator()
        elif choose=="chair":
            self.__admin = ChairAdministrator()
        else:
            pass