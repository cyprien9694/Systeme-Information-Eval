import grpc
from concurrent import futures
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.generated import giftball_pb2, giftball_pb2_grpc

class NoTokenServicer(giftball_pb2_grpc.NoTokenServiceServicer):

    def InsertToken(self, request, context):
        print("Jeton inséré")
        return giftball_pb2.MachineResponse(
            message="Jeton inséré",
            stock=request.stock,
            next_state="ONE_TOKEN"
        )

    def EjectToken(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Aucun jeton à retirer",
            stock=request.stock,
            next_state="NO_TOKEN"
        )

    def TurnCrank(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Insérez un jeton d'abord",
            stock=request.stock,
            next_state="NO_TOKEN"
        )

    def Dispense(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Impossible",
            stock=request.stock,
            next_state="NO_TOKEN"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    giftball_pb2_grpc.add_NoTokenServiceServicer_to_server(NoTokenServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("NoTokenService démarré sur le port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()