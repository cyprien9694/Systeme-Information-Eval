from src.giftball import GiftBall
from src.state import State

def test_insert_token():
    machine = GiftBall(2)
    machine.insert_token()
    assert machine.current_state == State.ONE_TOKEN

def test_dispense():
    machine = GiftBall(1)
    machine.insert_token()
    machine.turn_crank()
    assert machine.stock == 0
    assert machine.current_state == State.EMPTY

def test_eject_token():
    machine = GiftBall(2)
    machine.insert_token()
    machine.eject_token()
    assert machine.current_state == State.NO_TOKEN