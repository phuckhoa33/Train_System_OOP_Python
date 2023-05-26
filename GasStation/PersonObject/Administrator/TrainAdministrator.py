from GasStation.PersonObject.Administrator.Adminstrator import Administrator


class TrainAdministrator(Administrator):

    def __init__(self) -> None:
        super().__init__()

    def create(self):
        try:
            self._database.connect()
            # Get all train_name 
            query = "SELECT train_name FROM train"
            result = self._database.query_have_return(query)

            # Create a new train
            while True:
                train_name = input("What name do you want to create:")
                if train_name not in result['train_name']:
                    break
            
            # Check duplicated name train 

            query = f"INSERT INTO train(train_name) VALUES (%s)"
            val = (train_name)
            self._database.query_have_not_return(query, val) 
            print("Create train is successful")
            

            self._database.disconnect()
        except Exception as e:
            print(f"Create train is failed and {e}")

    def delete(self):
        return super().delete()
    
    def update(self):
        return super().update()