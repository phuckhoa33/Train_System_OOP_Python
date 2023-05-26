from Interface.PersonInterface import PartAdministratorInterface
from caching.GlobalStorage import global_storage
from Interface.DatabaseInterface import DatabaseConnection

class Administrator(PartAdministratorInterface):
    def __init__(self) -> None:
        self._database: DatabaseConnection = global_storage.get('database')

    def create(self, wagon_id):
        return super().create(wagon_id)
    
    def delete(self, wagon_id):
        return super().delete(wagon_id)
    
    def update(self, wagon_id):
        return super().update(wagon_id)