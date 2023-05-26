from GasStation.Train.Wagon.WagonManagementSystem.AbstractClass.WagonManagementSystemBaseClass import WagonManagementSystemBaseClass
from Interface.DatabaseInterface import DatabaseConnection

class PassengerManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int) -> None:
        super().__init__(code)

    @property
    def __type_chair(self):
        self.database.connect()
        query = f"SELECT chair_type FROM chair WHERE wagon_id = {self.code}"
        result = self.database.query_have_return(query)
        self.database.disconnect()
        return result[0]['chair_type']
    
    def create_new_chair_or_room_or_insert_goods(self):
        self._admin.create_new_chair(self.code, self.__type_chair)