from GasStation.Train.Wagon.WagonManagementSystem.AbstractClass.WagonManagementSystemBaseClass import WagonManagementSystemBaseClass
from Interface.DatabaseInterface import DatabaseConnection

class HeadHeadManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int, database: DatabaseConnection) -> None:
        super().__init__(code, database)

    def create_new_chair_or_room_or_insert_goods(self, type: str):
        self.database.connect()
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
        val = (self.code, 0, 'waiting', type)
        self.database.query_have_not_return(query, val)
        self.database.disconnect()


class TailHeadManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int, database: DatabaseConnection) -> None:
        super().__init__(code, database)
    
    def create_new_chair_or_room_or_insert_goods(self, type: str):
        self.database.connect()
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
        val = (self.code, 0, 'waiting', type)
        self.database.query_have_not_return(query)
        self.database.disconnect()
