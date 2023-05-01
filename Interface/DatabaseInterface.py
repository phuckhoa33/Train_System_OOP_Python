from abc import ABCMeta, abstractmethod
from dotenv import load_dotenv
import os 

load_dotenv()

class DatabaseConnection(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.__get_environment_variables()

    def __get_environment_variables(self):
        self.database_host = os.getenv('DATABASE_HOST')
        self.database_name = os.getenv('DATABASE_NAME')
        self.database_password = os.getenv('DATABASE_PASSWORD')
        self.database_user = os.getenv('DATABASE_USER')


    @abstractmethod
    def connect(self):
        pass 

    @abstractmethod
    def disconnect(self):
        pass 

    @abstractmethod
    def query_have_return(self, query: str):
        pass 

    @abstractmethod
    def query_have_not_return(self, query: str):
        pass 
