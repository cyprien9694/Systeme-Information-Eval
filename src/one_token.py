from src.state import State

class OneTokenState(State):

    def insert_token(self, machine):
        print("Déjà un jeton")

    def eject_token(self, machine):
        print("Jeton rendu")
        from src.no_token import NoTokenState
        machine.set_state(NoTokenState())

    def turn_crank(self, machine):
        print("Manivelle tournée")
        from src.dispensing import DispensingState
        machine.set_state(DispensingState())
        machine.state.dispense(machine)

    def dispense(self, machine):
        print("Impossible")