from TrainManagementSystem import TrainManagementSystem

class Train():
    def __init__(self, train_name: str, code: int) -> None:
        self.__train_name = train_name
        self.__code = code 
        self.__manager = TrainManagementSystem(code)

    def display(self) -> str:
        return ""