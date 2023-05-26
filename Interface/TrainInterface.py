from abc import ABC, abstractmethod

class TrainInterface(ABC):

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_list_of_workers(self):
        pass

    @abstractmethod
    def display_all_information(self):
        pass 