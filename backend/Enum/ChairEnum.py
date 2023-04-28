from enum import Enum

class ChairState(Enum):
    ACTIVE: str = "active"
    WAITED: str = "waiting"
    UNACTIVE: str = "unactive"

class ChairType(Enum):
    HARD: str = "hard"
    SOFT: str = "soft"
    ROOM: str = "room"