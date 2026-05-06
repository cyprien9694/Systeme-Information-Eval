from src.giftball import GiftBall
from src.no_token import NoTokenState
from src.one_token import OneTokenState
from unittest.mock import patch

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

def test_double_dispense():
    machine = GiftBall(3)
    machine.insert_token()
    with patch('random.random', return_value=0.10): 
        machine.turn_crank()
    assert machine.stock == 1 
    assert isinstance(machine.state, NoTokenState)