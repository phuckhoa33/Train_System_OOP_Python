from GasStation.Train.Wagon.WagonManagementSystem.AbstractClass.WagonManagementSystemBaseClass import WagonManagementSystemBaseClass
from Interface.DatabaseInterface import DatabaseConnection

class HeadHeadManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int) -> None:
        super().__init__(code)

    def create_new_chair_or_room_or_insert_goods(self):
        type = input("What type chair do you want to add: ")
        if type not in ['hard', 'room', 'soft']:
            print("Invalid chair type")
        else:
            self._admin.create_new_chair(self.code, type)


class TailHeadManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int) -> None:
        super().__init__(code)
    
    def create_new_chair_or_room_or_insert_goods(self):
        type = input("What type chair do you want to add: ")
        if type not in ['hard', 'room', 'soft']:
            print("Invalid chair type")
        else:
            self._admin.create_new_chair(self.code, type)
