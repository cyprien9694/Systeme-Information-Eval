from abc import ABC, abstractmethod

class State(ABC):

    @abstractmethod
    def insert_token(self, machine): pass

    @abstractmethod
    def eject_token(self, machine): pass

    @abstractmethod
    def turn_crank(self, machine): pass

    @abstractmethod
    def dispense(self, machine): pass