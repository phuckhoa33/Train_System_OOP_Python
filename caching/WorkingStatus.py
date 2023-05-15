from Interface.JsonInterface import JsonProcessingInterface
class WorkingStatus:
    def __init__(self, data: dict) -> None:
        self.__data = data 

    def choose_driver(self):
        return self.__data.get('driver') 

    def choose_co_driver(self):
        return self.__data.get('co_driver')

    def choose_waiter(self):
        return self.__data.get('waiter')