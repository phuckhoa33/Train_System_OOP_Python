from GasStation.Train.Wagon.WagonManagementSystem.AbstractClass.WagonManagementSystemBaseClass import WagonManagementSystemBaseClass
from Interface.DatabaseInterface import DatabaseConnection

class RestaurantManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int) -> None:
        super().__init__(code)
    
    def create_new_chair_or_room_or_insert_goods(self):
        self._admin.create_new_chair(self.code, 'hard')