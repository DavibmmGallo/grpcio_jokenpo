from __future__ import print_function

import logging
import grpc
import resources.game_pb2 as game_pb2
import resources.game_pb2_grpc as game_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = game_pb2_grpc.AnalizerStub(channel)
        v = str(input('Value [S (scissors), R (Rock), P (Paper)] : '))
        stub.SendHand(game_pb2.Hand(value=v))
        response = stub.getWinner(game_pb2.void())
    
    if response.value == 'Tie':
        print("Empate!")
    else:
        if response.value == v:
            print(f"Ganhou! {response.value} | {v}")
        else:
            print(f"Perdeu! {response.value} | {v}")
    


if __name__ == '__main__':
    logging.basicConfig()
    run()