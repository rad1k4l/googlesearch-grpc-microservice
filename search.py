from googlesearch import search
from concurrent import futures
import logging

import google_pb2_grpc
import google_pb2
import grpc
import argparse


class GoogleSearcherService(google_pb2_grpc.GoogleSearcherServicer):

    def search(self, request, context):
        results = []
        for url in search(request.query, stop=request.stop):
            results.append(url)
        response = google_pb2.GoogleSearchResponse()
        response.results.extend(results)
        return response


# parse arguments from command line
# returns object, properties:
#   addr - type string, grpc serving address
def getConfig():
    parser = argparse.ArgumentParser(description='Google Search grpc service')
    parser.add_argument('--address', dest='addr',
                        type=str,
                        help='Service listen address. Default value is localhost:42420', default="localhost:42420")

    return parser.parse_args()


def serve():
    config = getConfig()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    google_pb2_grpc.add_GoogleSearcherServicer_to_server(
        GoogleSearcherService(), server)
    server.add_insecure_port(config.addr)
    server.start()
    logging.info(f'gRPC service started at {config.addr}')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    serve()
