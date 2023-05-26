from Enum.GenderEnum import GenderState
from GasStation.PersonObject.AbstractClass.PersonAbstractClass import PersonBaseClass
from Enum.PersonEnum import PersonEnum
from Interface.PersonInterface import AdminInterface
from Interface.DatabaseInterface import DatabaseConnection
from caching.GlobalStorage import global_storage

class Admin(PersonBaseClass, AdminInterface):
    def __init__(self, email: str, fullname: str, code: int, telephoneNumber: str, gender: GenderState) -> None:
        super().__init__(email, fullname, code, telephoneNumber, gender)
        self.update_type(PersonEnum.ADMIN)
        self.database: DatabaseConnection = global_storage.get('database')

    def create_new_chair(self, wagon_id, chair_type: str):
        self.database.connect()
        query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
        val = (wagon_id, 0, 'waiting', chair_type)
        self.database.query_have_not_return(query, val) 
        self.database.disconnect()
    
    def create_new_train(self):
        try:
            self.database.connect()
            # Get all train_name 
            query = "SELECT train_name FROM train"
            result = self.database.query_have_return(query)

            # Create a new train
            while True:
                train_name = input("What name do you want to create:")
                if train_name not in result['train_name']:
                    break
            
            # Check duplicated name train 

            query = f"INSERT INTO train(train_name) VALUES (%s)"
            val = (train_name)
            self.database.query_have_not_return(query, val) 
            print("Create train is successful")
            

            self.database.disconnect()
        except Exception as e:
            print(f"Create train is failed and {e}")

    def create_new_chair(self, wagon_id):
        try:
            self.database.connect()
            query = f"INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (%s, %s, %s, %s)"
            val = (wagon_id, 0, 'waiting', 'hard')
            self.database.query_have_not_return(query, val) 
            self.database.disconnect()
        except Exception as e:
            print(f"Create chair is failed and {e}")
    
    def create_new_wagon(self, train_id: int, wagon_type: str, width, height, length):
        try:
            self.database.connect()
            query = "INSERT INTO wagon(train_id, width, height, length, wagon_type) VALUES (%s, %s, %s, %s, %s)"
            val = (train_id, width, height, length, wagon_type)
            self.database.query_have_not_return(query, val) 
            self.database.disconnect()
        except Exception as e:
            print(f"Create wagon is failed and {e}")