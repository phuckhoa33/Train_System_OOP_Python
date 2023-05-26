from Interface.PersonInterface import PartAdministratorInterface, UserInterface
from caching.GlobalStorage import global_storage
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

    def user(self, part: str):
        while True:
            print("-------------------------------------")
            print(
                f"\nThis is user catalog of {part} part\n \
                    1. Find \n \
                    2. Buy \n\
                    3. Recharge\n\
                    4. Cancle\n"
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

    def admin(self, part: str):
        while True:
            print("-------------------------------------")
            print(
                f"\nThis is admin catalog of {part} part\n\
                    1. Find\n\
                    2. Create\n\
                    3. Update\n\
                    4. Delete\n"
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