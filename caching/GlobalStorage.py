from Interface.GlobalStorageInterface import GlobalStorageInterface

class GlobalStorage(GlobalStorageInterface):
    def __init__(self) -> None:
        self.__storage = {}

    def add(self, attribute: object, name: str):
        self.__storage[name] = attribute
    
    def remove(self, name: str):
        del self.__storage[name]
    
    def update(self, attribute: object, name: str):
        self.__storage[name] = attribute
    
    def get(self, attribute: str):
        return self.__storage[attribute]

global_storage = GlobalStorage()    