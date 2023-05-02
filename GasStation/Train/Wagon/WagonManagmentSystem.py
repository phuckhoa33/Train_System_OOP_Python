from abc import ABC, abstractmethod
from Enum.WagonEnum import WagonType
from Interface.WagonInterface import WagonManagementSystem



class HeadHeadManagementSystem(WagonManagementSystem):
    def __init__(self, code: int) -> None:
        super().__init__(code)
    
    def find_information_of_chair_room_goods(self, code: int):
        pass 

    
    def create_new_chair_or_room_or_insert_goods(self, code: int):
        pass 

    
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 

class TailHeadManagementSystem(WagonManagementSystem):
    def __init__(self, code: int) -> None:
        super().__init__(code)
    
    def find_information_of_chair_room_goods(self, code: int):
        pass 

    
    def create_new_chair_or_room_or_insert_goods(self, code: int):
        pass 

    
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 

class PassengerManagementSystem(WagonManagementSystem):
    def __init__(self, code: int) -> None:
        super().__init__(code)

    def find_information_of_chair_room_goods(self, code: int):
        pass 

    
    def create_new_chair_or_room_or_insert_goods(self, code: int):
        pass 

    
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 

class RestaurantManagementSystem(WagonManagementSystem):
    def __init__(self, code: int) -> None:
        super().__init__(code)
        
    def find_information_of_chair_room_goods(self, code: int):
        pass 

    
    def create_new_chair_or_room_or_insert_goods(self, code: int):
        pass 

    
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 

class CargoManagementSystem(WagonManagementSystem):
    def __init__(self, code: int) -> None:
        super().__init__(code)

    def find_information_of_chair_room_goods(self, code: int):
        pass 

    
    def create_new_chair_or_room_or_insert_goods(self, code: int):
        pass 

    
    def update_state_of_chair_or_room_or_insert_goods(self, code: int):
        pass 