from abc import ABC, abstractmethod

class JsonProcessingInterface(ABC):

    @abstractmethod
    def add_new_value(self, new_value: dict):
        pass

    @abstractmethod
    def eliminate_a_value(self, key, value):
        pass

    @abstractmethod
    def check_exist_value(self, key):
        pass