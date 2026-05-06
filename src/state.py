from enum import Enum, auto

class State(Enum):
    NO_TOKEN = auto()
    ONE_TOKEN = auto()
    DISPENSING = auto()
    EMPTY = auto()