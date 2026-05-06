class GiftBall:

    def __init__(self, stock=5):
        self.stock = stock
        from src.no_token import NoTokenState
        self.state = NoTokenState()

    def set_state(self, state):
        self.state = state

    def insert_token(self):
        self.state.insert_token(self)

    def eject_token(self):
        self.state.eject_token(self)

    def turn_crank(self):
        self.state.turn_crank(self)

    def release_ball(self):
        if self.stock > 0:
            self.stock -= 1

    def is_empty(self):
        return self.stock <= 0