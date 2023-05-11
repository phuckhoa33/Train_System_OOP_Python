from abc import ABC, abstractmethod

class TrainInterface(ABC):

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def __get_list_of_workers(self):
        pass