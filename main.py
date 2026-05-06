from src.giftball import GiftBall

def main():
    machine = GiftBall(stock=3)

    machine.insert_token()
    machine.turn_crank()

    machine.insert_token()
    machine.eject_token()

    machine.insert_token()
    machine.turn_crank()

    machine.insert_token()
    machine.turn_crank()

    machine.insert_token() 

if __name__ == "__main__":
    main()