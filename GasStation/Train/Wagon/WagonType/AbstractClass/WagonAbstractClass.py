from abc import ABC, abstractmethod
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
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
        self.isFull = self.__manager.get_full_state()

    def display_catalog(self, person: PersonBaseClass):
        if person.type==PersonEnum.USER:
            self.__manager.user_catalog(person)
        elif person.type==PersonEnum.ADMIN:
            self.__manager.admin_catalog(person)
        return

    @abstractmethod
    def display(self):
        pass 