from configuration.Database import MysqlDatabaseConnection
from GasStation.Train.Wagon.Wagon import FirstHead, LastHead, Passenger, Restaurant, Cargo

class TrainManagementSystem():
    def __init__(self, code: int) -> None:
        self.__code = code 
        self.database = MysqlDatabaseConnection()

    @property
    def __data(self):
        self.database.connect()
        query = f"SELECT train_id, width, height, length, wagon_type FROM wagon WHERE train_id = {self.__code}"
        wagons = self.database.query_have_return(query)
        self.database.disconnect()
        return wagons

    @property
    def __wagons(self):

        D_wagon = {}
        for wagon in self.__data:
            checked_wagon = None 
            wagon_id = int(wagon['wagon_id'])
            width = int(wagon['width'])
            height = int(wagon['height'])
            length = int(wagon['length'])

            if wagon['wagon_type']=="firsthead":
                checked_wagon = FirstHead(wagon_id, width, height, length)
            elif wagon['wagon_type']=="lasthead":
                checked_wagon = LastHead(wagon_id, width, height, length)
            elif wagon['wagon_type']=="passenger":
                checked_wagon = Passenger(wagon_id, width, height, length)
            elif wagon['wagon_type']=="restaurant":
                checked_wagon = Restaurant(wagon_id, width, height,length)
            elif wagon['wagon_type']=="cargo":
                checked_wagon = Cargo(wagon_id, width, height, length)
            
            D_wagon[wagon_id] = checked_wagon

    def __create_wagon(self):
        pass 

    def __find_wagon(self):
        pass 

    def catalog(self):
        pass 