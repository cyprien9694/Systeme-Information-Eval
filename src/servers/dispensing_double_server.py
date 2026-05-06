import grpc
from concurrent import futures
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.generated import giftball_pb2, giftball_pb2_grpc

class DispensingDoubleServicer(giftball_pb2_grpc.DispensingDoubleServiceServicer):

    def InsertToken(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Veuillez attendre",
            stock=request.stock,
            next_state="DISPENSING_DOUBLE"
        )

    def EjectToken(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Impossible, distribution en cours",
            stock=request.stock,
            next_state="DISPENSING_DOUBLE"
        )

    def TurnCrank(self, request, context):
        return giftball_pb2.MachineResponse(
            message="Déjà en cours",
            stock=request.stock,
            next_state="DISPENSING_DOUBLE"
        )

    def Dispense(self, request, context):
        new_stock = max(request.stock - 2, 0)
        print("2 balles surprise distribuées !")
        return giftball_pb2.MachineResponse(
            message="2 balles surprise distribuées !",
            stock=new_stock,
            next_state="NO_TOKEN"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    giftball_pb2_grpc.add_DispensingDoubleServiceServicer_to_server(DispensingDoubleServicer(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    print("DispensingDoubleService démarré sur le port 50054")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()