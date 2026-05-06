from src.state import State

class GiftBall:
    def __init__(self, stock=5):
        self.stock = stock
        self.current_state = State.NO_TOKEN if stock > 0 else State.EMPTY

    def insert_token(self):
        if self.current_state == State.NO_TOKEN:
            self.current_state = State.ONE_TOKEN
            print("Jeton inséré.")
        elif self.current_state == State.ONE_TOKEN:
            print("Vous avez déjà inséré un jeton.")
        elif self.current_state == State.EMPTY:
            print("Machine vide.")
        else:
            print("Action impossible.")

    def eject_token(self):
        if self.current_state == State.ONE_TOKEN:
            self.current_state = State.NO_TOKEN
            print("Jeton récupéré.")
        else:
            print("Aucun jeton à éjecter.")

    def turn_crank(self):
        if self.current_state == State.ONE_TOKEN:
            print("Manivelle tournée...")
            self.current_state = State.DISPENSING
            self.dispense()
        elif self.current_state == State.NO_TOKEN:
            print("Insérez un jeton d'abord.")
        elif self.current_state == State.EMPTY:
            print("Machine vide.")
        else:
            print("Veuillez patienter.")

    def dispense(self):
        if self.current_state == State.DISPENSING:
            if self.stock > 0:
                self.stock -= 1
                print("Une balle surprise est distribuée !")

                if self.stock == 0:
                    self.current_state = State.EMPTY
                    print("La machine est maintenant vide.")
                else:
                    self.current_state = State.NO_TOKEN
            else:
                self.current_state = State.EMPTY
                print("Machine vide.")