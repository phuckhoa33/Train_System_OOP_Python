from Enum.PersonEnum import PersonEnum
from Interface.PersonInterface import PartAdministratorInterface
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
from caching.GlobalStorage import global_storage
from Interface.DatabaseInterface import DatabaseConnection

class Administrator(PartAdministratorInterface, PersonBaseClass):
    def __init__(self) -> None:
        self._database: DatabaseConnection = global_storage.get('database')
        self.update_type(PersonEnum.ADMIN)

    def create(self, wagon_id):
        return super().create(wagon_id)
    
    def delete(self, wagon_id):
        return super().delete(wagon_id)
    
    def update(self, wagon_id):
        return super().update(wagon_id)