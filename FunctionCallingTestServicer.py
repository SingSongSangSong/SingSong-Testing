from locust import events, task

import gevent
from gRPCInterceptor import GrpcUser
from proto.functionCallingRecommend.functionCallingRecommend_pb2 import FunctionCallingRequest, FunctionCallingResponse
from proto.functionCallingRecommend.functionCallingRecommend_pb2_grpc import functionCallingRecommendStub, functionCallingRecommendServicer, add_functionCallingRecommendServicer_to_server


class HelloGrpcUser(GrpcUser):
    host = "localhost:50051"
    stub_class = functionCallingRecommendStub

    @task
    def GetFunctionCallingRecommendation(self):
        self.stub.GetFunctionCallingRecommendation(FunctionCallingRequest(memberId=1, command="command"))