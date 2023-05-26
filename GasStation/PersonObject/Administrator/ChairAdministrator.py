from GasStation.PersonObject.Administrator.Adminstrator import Administrator
from caching.GlobalStorage import global_storage
from Interface.DatabaseInterface import DatabaseConnection


class ChairAdministrator(Administrator):

    def __init__(self) -> None:
        super().__init__()

    def create(self, wagon_id):
        try:
            self._database.connect()
            query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
            val = (wagon_id, 0, 'waiting', 'hard')
            self._database.query_have_not_return(query, val) 
            self._database.disconnect()
        except Exception as e:
            print(f"Create chair is failed and {e}")

    def update(self, wagon_id):
        return super().update(wagon_id)
    
    def delete(self, wagon_id):
        return super().delete(wagon_id)