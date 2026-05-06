from src.state import State

class DispensingState(State):

    def insert_token(self, machine):
        print("Veuillez attendre")

    def eject_token(self, machine):
        print("Impossible, distribution en cours")

    def turn_crank(self, machine):
        print("Déjà en cours")

    def dispense(self, machine):
        from src.no_token import NoTokenState
        machine.release_ball()
        print("Balle surprise distribuée !")
        machine.set_state(NoTokenState())