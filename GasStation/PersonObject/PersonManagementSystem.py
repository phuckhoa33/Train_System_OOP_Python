from Interface.PersonManagementSystemInterface import PersonManagementSystem
from configuration.Database import MysqlDatabaseConnection
from GasStation.PersonObject.User import User


class UserManagementSystem(PersonManagementSystem):
    def __init__(self) -> None:
        super().__init__()
        self.__database = None
        self.__database.connect()

    def find(self, code: int):
        query = f"SELECT * FROM user WHERE user_id = '{code}'"
        result = self.__database.query_have_return(query)
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