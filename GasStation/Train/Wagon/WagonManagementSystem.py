from AbstractClass.WagonAbstractClass import WagonManagementSystemBaseClass

class HeadHeadManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int) -> None:
        super().__init__(code)

    def create_new_chair_or_room_or_insert_goods(self, type: str):
        self.database.connect()
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
        val = (self.code, 0, 'waiting', type)
        self.database.query_have_not_return(query, val)
        self.database.disconnect()


class TailHeadManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int) -> None:
        super().__init__(code)
    
    def create_new_chair_or_room_or_insert_goods(self, type: str):
        self.database.connect()
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
        val = (self.code, 0, 'waiting', type)
        self.database.query_have_not_return(query)
        self.database.disconnect()


class PassengerManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int, type: str) -> None:
        super().__init__(code)
        self.__type_chair = type
    
    def create_new_chair_or_room_or_insert_goods(self):
        self.database.connect()
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
        val = (self.code, 0, 'waiting', self.__type_chair)
        self.database.query_have_not_return(query, val) 
        self.database.disconnect()

    


class RestaurantManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int) -> None:
        super().__init__(code)
    
    def create_new_chair_or_room_or_insert_goods(self):
        self.database.connect()
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
        val = (self.code, 0, 'waiting', 'hard')
        self.database.query_have_not_return(query, val) 
        self.database.disconnect()
    


class CargoManagementSystem(WagonManagementSystemBaseClass):
    def __init__(self, code: int) -> None:
        super().__init__(code)

    
    def create_new_chair_or_room_or_insert_goods(self):
        self.database.connect()
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
        val = (self.code, 0, 'waiting', 'hard')
        self.database.query_have_not_return(query, val) 
        self.database.disconnect()