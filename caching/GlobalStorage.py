from Interface.GlobalStorageInterface import GlobalStorageInterface

class GlobalStorage(GlobalStorageInterface):
    def __init__(self) -> None:
        self.storage = {}

    def add(self, attribute: object, name: str):
        return super().add(attribute, name)
    
    def remove(self, attribute: object, name: str):
        return super().remove(attribute, name)
    
    def update(self, attribute: object, name: str):
        return super().update(attribute, name)
    
    def get(self, attribute: str):
        return super().get(attribute)

global_storage = GlobalStorage()    