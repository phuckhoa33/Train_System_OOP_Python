from Enum.ChairEnum import ChairState, ChairType
from Interface.UserInterface import PersonInterface
from abc import ABC, abstractmethod
from User.User import User

class Chair(ABC):
    def __init__(self) -> None:
        raise NotImplementedError("Cannot instantiate this class")

    def _set_ownership(self, owner: PersonInterface) -> None:
        self._owner = owner
        self._update_state(ChairState.ACTIVE)

    def _update_state(self, state: ChairState) -> None:
        self._state = state
        

class HardChair(Chair):
    def __init__(self, code: str) -> None:
        self.code = code
        self._type = ChairType.HARD

class SoftChair(Chair):
    def __init__(self, code: str) -> None:
        self.code = code
        self._type = ChairType.SOFT

class Room(Chair):
    def __init__(self, code: str) -> None:
        self.code = code
        self._type = ChairType.ROOM
