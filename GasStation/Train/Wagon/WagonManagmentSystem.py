from abc import ABC, abstractmethod
from Enum.WagonEnum import WagonType
from Interface.WagonInterface import WagonManagementSystem



class HeadHeadManagementSystem(WagonManagementSystem):
    def __init__(self, code: int) -> None:
        super().__init__(code)

    def create_new_chair_or_room_or_insert_goods(self):
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES ({self.code}, 0, 'waiting', 'firsthead')"
        self.database.query_have_not_return(query)

    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 

class TailHeadManagementSystem(WagonManagementSystem):
    def __init__(self, code: int) -> None:
        super().__init__(code)
    
    def create_new_chair_or_room_or_insert_goods(self):
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES ({self.code}, 0, 'waiting', 'tailhead')"
        self.database.query_have_not_return(query)

    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 

class PassengerManagementSystem(WagonManagementSystem):
    def __init__(self, code: int) -> None:
        super().__init__(code)

    
    def create_new_chair_or_room_or_insert_goods(self):
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES ({self.code}, 0, 'waiting', 'passenger')"
        self.database.query_have_not_return(query)

    
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 

class RestaurantManagementSystem(WagonManagementSystem):
    def __init__(self, code: int) -> None:
        super().__init__(code)
    
    def create_new_chair_or_room_or_insert_goods(self):
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES ({self.code}, 0, 'waiting', 'restaurant')"
        self.database.query_have_not_return(query)

    
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 

class CargoManagementSystem(WagonManagementSystem):
    def __init__(self, code: int) -> None:
        super().__init__(code)

    
    def create_new_chair_or_room_or_insert_goods(self):
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES ({self.code}, 0, 'waiting', 'cargo')"
        self.database.query_have_not_return(query)
    
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 