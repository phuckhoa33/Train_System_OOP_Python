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
        rows = self.__cursor.fetchall()
        columns = [desc[0] for desc in self.__cursor.description]
        result = []
        for row in rows:
            d = {}
            for i, column in enumerate(columns):
                d[column] = row[i]
            result.append(d)

        return result

    def query_have_not_return(self, query: str, val: tuple):
        self.__cursor.execute(query, val)
        self.__cnx.commit()