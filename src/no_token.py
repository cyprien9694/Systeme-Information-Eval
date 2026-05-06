from src.state import State

class NoTokenState(State):

    def insert_token(self, machine):
        print("Jeton inséré")
        from src.one_token import OneTokenState
        machine.set_state(OneTokenState())

    def eject_token(self, machine):
        print("Aucun jeton à retirer")

    def turn_crank(self, machine):
        print("Insérez un jeton d'abord")

    def dispense(self, machine):
        print("Impossible")