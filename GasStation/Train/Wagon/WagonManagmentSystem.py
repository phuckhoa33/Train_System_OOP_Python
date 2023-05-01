from abc import ABC, abstractmethod
from Enum.WagonEnum import WagonType
from Interface.WagonInterface import WagonManagementSystem



class HeadManagementSystem(WagonManagementSystem):
    def __init__(self, code: str) -> None:
        super().__init__(code)

class PassengerManagementSystem(WagonManagementSystem):
    def __init__(self, code: str) -> None:
        super().__init__(code)

class RestaurantManagementSystem(WagonManagementSystem):
    def __init__(self, code: str) -> None:
        super().__init__(code)

class CargoManagementSystem(WagonManagementSystem):
    def __init__(self, code: str) -> None:
        super().__init__(code)