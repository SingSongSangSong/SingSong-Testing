from locust import task, between
from gRPCInterceptor import GrpcUser
from proto.userProfileRecommend.userProfileRecommend_pb2 import ProfileRequest, ProfileResponse
from proto.userProfileRecommend.userProfileRecommend_pb2_grpc import UserProfileStub
import grpc
import random

class HelloGrpcUser(GrpcUser):
    host = "localhost:50051"  # gRPC 서버 주소
    stub_class = UserProfileStub  # 사용할 gRPC 스텁

    # 사용자 간 요청 간의 대기 시간 (1초~3초)
    wait_time = between(1, 3)

    @task
    def GetFunctionCallingRecommendation(self):
        try:
            # 무작위로 하나의 command 선택
            random_command = random.choice(self.commands)

            # 비동기 호출을 사용해 gRPC 요청 전송
            response_future = self.stub.GetFunctionCallingRecommendation.future(
                ProfileRequest(memberId=1, page=2, pageSize=10)
            )
            response = response_future.result(timeout=5)  # 5초 안에 응답 대기

            # 응답이 성공했을 때 Locust 이벤트 트리거
            self.environment.events.request.fire(
                request_type="gRPC",
                name="GetFunctionCallingRecommendation",
                response_time=0,  # 응답 시간 (측정 가능)
                response_length=len(response.SerializeToString()),
                exception=None,
            )

        except grpc.RpcError as e:
            # gRPC 오류 발생 시 Locust 이벤트에 예외 전달
            self.environment.events.request.fire(
                request_type="gRPC",
                name="GetFunctionCallingRecommendation",
                response_time=0,
                response_length=0,
                exception=e,
            )
            print(f"RPC Error: {e.code()} - {e.details()}")
    
    @task
    def CreateUserProfile(self):
        try:
            # 무작위로 하나의 command 선택
            random_command = random.choice(self.commands)

            # 비동기 호출을 사용해 gRPC 요청 전송
            response_future = self.stub.GetFunctionCallingRecommendation.future(
                FunctionCallingRequest(memberId=1, command=random_command)
            )
            response = response_future.result(timeout=5)  # 5초 안에 응답 대기

            # 응답이 성공했을 때 Locust 이벤트 트리거
            self.environment.events.request.fire(
                request_type="gRPC",
                name="GetFunctionCallingRecommendation",
                response_time=0,  # 응답 시간 (측정 가능)
                response_length=len(response.SerializeToString()),
                exception=None,
            )

        except grpc.RpcError as e:
            # gRPC 오류 발생 시 Locust 이벤트에 예외 전달
            self.environment.events.request.fire(
                request_type="gRPC",
                name="GetFunctionCallingRecommendation",
                response_time=0,
                response_length=0,
                exception=e,
            )
            print(f"RPC Error: {e.code()} - {e.details()}")