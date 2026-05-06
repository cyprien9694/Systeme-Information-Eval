import grpc
from concurrent import futures
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.generated import giftball_pb2, giftball_pb2_grpc

class DispensingServicer(giftball_pb2_grpc.DispensingServiceServicer):

    def InsertToken(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Veuillez attendre",
            stock=request.stock,
            next_state="DISPENSING"
        )

    def EjectToken(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Impossible, distribution en cours",
            stock=request.stock,
            next_state="DISPENSING"
        )

    def TurnCrank(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Déjà en cours",
            stock=request.stock,
            next_state="DISPENSING"
        )

    def Dispense(self, request, context):
        new_stock = request.stock - 1 if request.stock > 0 else 0
        print("Balle surprise distribuée !")
        return giftball_pb2.MachineResponse(
            message="Balle surprise distribuée !",
            stock=new_stock,
            next_state="NO_TOKEN"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    giftball_pb2_grpc.add_DispensingServiceServicer_to_server(DispensingServicer(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("DispensingService démarré sur le port 50053")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()