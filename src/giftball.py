import grpc
from src.generated import giftball_pb2, giftball_pb2_grpc

STATE_PORTS = {
    "NO_TOKEN": 50051,
    "ONE_TOKEN": 50052,
    "DISPENSING": 50053,
    "DISPENSING_DOUBLE": 50054,
}

class GiftBall:

    def __init__(self, stock=5):
        self.stock = stock
        self.current_state = "NO_TOKEN"

    def _get_stub(self):
        port = STATE_PORTS[self.current_state]
        channel = grpc.insecure_channel(f'localhost:{port}')
        stubs = {
            "NO_TOKEN": giftball_pb2_grpc.NoTokenServiceStub,
            "ONE_TOKEN": giftball_pb2_grpc.OneTokenServiceStub,
            "DISPENSING": giftball_pb2_grpc.DispensingServiceStub,
            "DISPENSING_DOUBLE": giftball_pb2_grpc.DispensingDoubleServiceStub,
        }
        return stubs[self.current_state](channel)

    def _call(self, action):
        stub = self._get_stub()
        request = giftball_pb2.MachineRequest(stock=self.stock)
        response = getattr(stub, action)(request)
        print(response.message)
        self.stock = response.stock
        self.current_state = response.next_state
        return response

    def insert_token(self):
        self._call("InsertToken")

    def eject_token(self):
        self._call("EjectToken")

    def turn_crank(self):
        resp = self._call("TurnCrank")
        self._call("Dispense")

    def is_empty(self):
        return self.stock <= 0