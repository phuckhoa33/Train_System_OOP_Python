from GasStation.Train.TrainManagementSystem import TrainManagementSystem
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
class Train():
    def __init__(self, train_name: str, code: int) -> None:
        self.train_name = train_name
        self.code = code 
        self.__manager = TrainManagementSystem(code)

    def display(self, user: PersonBaseClass) -> str:
        self.__manager.catalog(user)