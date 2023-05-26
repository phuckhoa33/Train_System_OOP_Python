from Interface.PersonManagementSystemInterface import PersonManagementSystem
from Interface.DatabaseInterface import DatabaseConnection
from GasStation.PersonObject.User import User
from caching.GlobalStorage import global_storage


class UserManagementSystem(PersonManagementSystem):
    def __init__(self) -> None:
        super().__init__()
        self.__database: DatabaseConnection = global_storage.get('database')

    def find(self, code: int):
        self.__database.connect()
        query = f"SELECT * FROM user WHERE user_id = '{code}'"
        result = self.__database.query_have_return(query)
        self.__database.disconnect()
        return result
    
    def mapping(self, code: int):
        user = self.find(code)
        for i in user:
            saved_user = User(i['email'], i['fullname'], i['user_id'], i['phoneNumber'], i['gender'])
        return saved_user        
    
    def update(self):
        return super().update()
    
    def create(self):
        return super().create()