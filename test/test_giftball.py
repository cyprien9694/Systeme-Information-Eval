from src.giftball import GiftBall
from src.no_token import NoTokenState
from src.one_token import OneTokenState

def test_insert_token():
    machine = GiftBall(2)
    machine.insert_token()
    assert isinstance(machine.state, OneTokenState)

def test_dispense():
    machine = GiftBall(1)
    machine.insert_token()
    machine.turn_crank()
    assert machine.stock == 0
    assert isinstance(machine.state, NoTokenState)

def test_eject_token():
    machine = GiftBall(2)
    machine.insert_token()
    machine.eject_token()
    assert isinstance(machine.state, NoTokenState)