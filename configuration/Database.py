import pymysql
import mysql.connector as connector
from Interface.DatabaseInterface import DatabaseConnection

class MysqlDatabaseConnection(DatabaseConnection):
    def __init__(self) -> None:
        super().__init__()


    def connect(self):
        self.__cnx = connector.connect(user=self.database_user, \
                                        password=self.database_password, \
                                        host=self.database_host, \
                                        database=self.database_name)
        self.__cursor = self.__cnx.cursor()
        
    def disconnect(self):
        self.__cursor.close()
        self.__cnx.close()
    
    def query_have_return(self, query):
        self.__cursor.execute(query)
        data_list = {}
        for (train_id, train_name) in self.__cursor:
            data_list.append((train_id, train_name))
        print(data_list)


        return data_list
    def query_have_not_return(self, query: str):
        self.__cursor.execute(query)