from googlesearch import search
from concurrent import futures
import logging

import google_pb2_grpc
import google_pb2
import grpc


class GoogleSearcherService(google_pb2_grpc.GoogleSearcherServicer):

    def search(self, request, context):
        results = []
        for url in search(request.query, stop=request.stop):
            results.append(url)
        response = google_pb2.GoogleSearchResponse()
        response.results.extend(results)
        return response


def serve():
    service_addr = '[::]:42420'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    google_pb2_grpc.add_GoogleSearcherServicer_to_server(
        GoogleSearcherService(), server)
    server.add_insecure_port(service_addr)
    server.start()
    logging.info(f'gRPC service started at {service_addr}')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    serve()
