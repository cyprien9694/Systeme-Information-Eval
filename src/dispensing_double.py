from src.state import State

class DispensingDoubleState(State):

    def insert_token(self, machine):
        print("Veuillez attendre")

    def eject_token(self, machine):
        print("Impossible, distribution en cours")

    def turn_crank(self, machine):
        print("Déjà en cours")

    def dispense(self, machine):
        from src.no_token import NoTokenState
        machine.release_ball()
        machine.release_ball()
        print("2 balles surprise distribuées !")
        machine.set_state(NoTokenState())