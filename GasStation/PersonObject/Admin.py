from Enum.GenderEnum import GenderState
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
from Enum.PersonEnum import PersonEnum
from Interface.PersonInterface import AdminInterface
from Interface.DatabaseInterface import DatabaseConnection

class Admin(PersonBaseClass, AdminInterface):
    def __init__(self, email: str, fullname: str, code: int, telephoneNumber: str, gender: GenderState, database: DatabaseConnection) -> None:
        super().__init__(email, fullname, code, telephoneNumber, gender)
        self.update_type(PersonEnum.ADMIN)
        self.database = database

    def grant_rights(self):
        return super().grant_rights()
    
    def create_new_train(self):
        pass

    def create_new_chair(self, wagon_id):
        self.database.connect()
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
        val = (wagon_id, 0, 'waiting', 'hard')
        self.database.query_have_not_return(query, val) 
        self.database.disconnect()
    
    def create_new_wagon(self, train_id: int):
        pass 