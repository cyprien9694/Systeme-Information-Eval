import grpc
import random
from concurrent import futures
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.generated import giftball_pb2, giftball_pb2_grpc

class OneTokenServicer(giftball_pb2_grpc.OneTokenServiceServicer):

    def InsertToken(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Déjà un jeton",
            stock=request.stock,
            next_state="ONE_TOKEN"
        )

    def EjectToken(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Jeton rendu",
            stock=request.stock,
            next_state="NO_TOKEN"
        )

    def TurnCrank(self, request, context):
        print("Manivelle tournée")
        next_state = "DISPENSING_DOUBLE" if random.random() < 0.20 else "DISPENSING"
        return giftball_pb2.MachineResponse(
            message="Manivelle tournée",
            stock=request.stock,
            next_state=next_state
        )

    def Dispense(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Impossible",
            stock=request.stock,
            next_state="ONE_TOKEN"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    giftball_pb2_grpc.add_OneTokenServiceServicer_to_server(OneTokenServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("OneTokenService démarré sur le port 50052")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()