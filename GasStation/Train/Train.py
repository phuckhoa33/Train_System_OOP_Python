from GasStation.Train.TrainManagementSystem import TrainManagementSystem
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
from Interface.TrainInterface import TrainInterface

class Train(TrainInterface):
    def __init__(self, train_name: str, code: int) -> None:
        self.train_name = train_name
        self.code = code 
        self.__manager = TrainManagementSystem(code)
        self.__get_list_of_workers()

    def __get_list_of_workers(self):
        self.__manager.get__workers(self)
        
    def get_list_of_workers(self):
        self.__get_list_of_workers()

    def display(self):
        print(f"The train code is {self.code}\
              Train name is {self.train_name}")