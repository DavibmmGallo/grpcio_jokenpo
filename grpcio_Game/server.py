# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide server."""

from concurrent import futures
import logging
import grpc
from resources import (
    game_pb2,
    game_pb2_grpc
)
from resources.joken import Jokenpo
from redis import Redis
import json


class GameServicer(game_pb2_grpc.AnalizerServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.count = 0
        self.requests = []
        self.r = Redis(host='redis-server',port=6379,db=0)

    def SendHand(self, request, context):
        self.requests.append(request.value)
        self.count+=1
        return game_pb2.void()

    def getWinner(self, request, context):
        while self.count%2!=0:
            self.wait = True
        self.wait = False
        win = Jokenpo(self.requests[self.count-2], self.requests[self.count-1])
        self.r.set('Round',json.dumps(
            {
                'player1': self.requests[self.count-2],
                'player2': self.requests[self.count-1]
            })
        )
        print('Round ' + str(json.loads(self.r.get('Round'))))
        return game_pb2.Hand(value=win)
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    game_pb2_grpc.add_AnalizerServicer_to_server(
        GameServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started!')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()