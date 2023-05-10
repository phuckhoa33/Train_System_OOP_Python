from GasStation.Train.Wagon.WagonManagementSystem.AbstractClass.WagonManagementSystemBaseClass import WagonManagementSystemBaseClass

class CargoManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int) -> None:
        super().__init__(code)

    
    def create_new_chair_or_room_or_insert_goods(self):
        self.database.connect()
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
        val = (self.code, 0, 'waiting', 'hard')
        self.database.query_have_not_return(query, val) 
        self.database.disconnect()