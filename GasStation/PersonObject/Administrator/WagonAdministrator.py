from GasStation.PersonObject.Administrator.Adminstrator import Administrator


class TrainAdministrator(Administrator):

    def __init__(self) -> None:
        super().__init__()

    def create(self, train_id: int):
        try:
            wagon_type = input("What wagon do you want to create: ")
            width = int(input("How many width: "))
            height = int(input("How many height: "))
            length = int(input("How many length: "))
            self._database.connect()
            query = "INSERT INTO wagon(train_id, width, height, length, wagon_type) VALUES (%s, %s, %s, %s, %s)"
            val = (train_id, width, height, length, wagon_type)
            self._database.query_have_not_return(query, val) 
            self._database.disconnect()
        except Exception as e:
            print(f"Create wagon is failed and {e}")
    
    def update(self, wagon_id):
        return super().update(wagon_id)
    
    def delete(self, wagon_id):
        return super().delete(wagon_id)