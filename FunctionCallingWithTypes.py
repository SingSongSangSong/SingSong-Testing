from locust import task, between
from gRPCInterceptor import GrpcUser
from proto.functionCallingWithTypes.functionCallingWithTypes_pb2 import FunctionCallingWithTypesRequest
from proto.functionCallingWithTypes.functionCallingWithTypes_pb2_grpc import FunctionCallingWithTypesRecommendStub
import grpc
import random

class HelloGrpcUser(GrpcUser):
    host = "localhost:50051"  # gRPC 서버 주소
    stub_class = FunctionCallingWithTypesRecommendStub  # 사용할 gRPC 스텁

    commands = [
        "노래방에서 분위기 띄우기 좋은 신나는 곡 추천해줘",
        "신나는 느낌의 노래 추천해줘",
        "2010년도 초반노래 추천해줘",
        "2010년도 초반 아이돌 노래 추천해줘",
        "신나는데 고음있고 가사는 애절한 노래",
        "고음 자신 있는데, 고음 폭발하는 곡 추천해줘",
        "노래방에서 부르기 쉬운 발라드 추천해줘",
        "밴드노래",
        "난 고칠수없는 병에걸렸어",
        "데이식스 Happy 같은 노래 추천좀",
        "노래방에서 첫곡으로 부를수 있는 케이팝 노래 추천해줘",
        "일본곡",
        "2010년대 일본 음악",
        "인기 있는 일본 음악",
        "Ado",
        "2010년도 쯤에 신나는 노래 추천해줘",
        "부르기 쉬운 발라드",
        "노래방에서 분위기 띄우기 좋은 신나는 곡 추천해줘",
        "제목에 '레몬'이 들어간 노래",
        "요네즈 켄시 노래 추천해줘",
        "혼자 노래방 갈 때 부르기 좋은 노래 있을까?",
        "랩",
        "느린심장박동 같은",
        "Kpop",
        "낮은 남자노래",
        "소수빈",
        "옛날 노래방 인기곡 중에서 부르기 좋은 노래 뭐 있어?",
        "노래방에서 분위기 띄우기 좋은 신나는 곡 추천해줘",
        "노래방에서 부르기 쉬운 발라드 추천해줘",
        "'꿈속에 너' 같은 노래 추천해줘",
        "노래방에서 부르기 쉬운 발라드 추천해줘",
        "부르기 쉬운 세븐틴 노래 발라드 느낌",
        "어디에도",
        "요즘 노래방에서 유행하는 핫한 곡 추천해줘",
        "노래방에서 부르기 쉬운 발라드 추천해줘",
        "노래방에서 부르기 쉬운 발라드 추천해줘",
        "노래방에서 부르기 쉬운 유ㅇ발라드 추천해줘",
        "오늘 헤어졌는데 부를만한 노래 추천좀..",
        "노래방에서 부르기 쉬운 유명한 발라드 추천해줘",
        "10대들이 부르는 발라드",
        "안예은",
        "발라드 말고, 락 느낌 나는 노래방 곡 추천 좀!",
        "저음도 잘 부르는 편인데, 저음 매력적인 노래 뭐 있어?",
        "랩",
        "모두 아는 랩",
        "잘 때 듣기 좋은 노래 추천해줘",
        "요즘 노래방에서 유행하는 핫한 곡 추천해줘",
        "혼자 노래방 갈 때 부르기 좋은 노래 있을까?",
        "노래방에서 부르기 쉬운 발라드 추천해줘",
        "세븐틴 노래 추천해줘",
        "애절한 감성 가득한 노래 추천해줘, 부르고 싶어",
        "친구들이랑 신나게 부를 수 있는 노래 알려줘",
        "갬성힙합",
        "감성 충만한 발라드 추천해줘, 노래방에서 부르고 싶어",
        "요즘 노래방에서 유행하는 핫한 곡 추천해줘",
        "오늘 헤어졌는데 부를만한 노래 추천좀..",
        "노래방에서 부르기 쉬운 발라드 추천해줘",
        "친구들이랑 신나게 부를 수 있는 노래 알려줘",
        "노래방 부르기 좋은 노래",
        "버즈의 가시나 박효신의 동경과 같은 노래 추천해줘",
        "요즘 유행하는 K-POP",
        "2010년도 쯤에 신나는 노래 추천해줘",
        "오늘 헤어졌는데 부를만한 노래 추천좀..",
        "감성 충만한 노래 추천해줘",
        "락발라드 추천해줘",
        "고음 자신 있는데, 고음 폭발하는 곡 추천해줘",
        "발라드 말고, 락 느낌 나는 노래방 곡 추천 좀!",
        "저음도 잘 부르는 편인데, 저음 매력적인 노래 뭐 있어?",
        "내 사랑이 그대로인것처렁",
        "오래전에 함께듣던 노래가",
        "나에게로 떠나는 여행 같은 노래 추천",
        "노래방에서 부르기 쉬운 발라드 추천해줘"
    ]

    # 사용자 간 요청 간의 대기 시간 (1초~3초)
    wait_time = between(1, 3)

    @task
    def GetFunctionCallingWithTypesRecommendation(self):
        try:
            # 무작위로 하나의 command 선택
            random_command = random.choice(self.commands)

            # 비동기 호출을 사용해 gRPC 요청 전송
            response_future = self.stub.GetFunctionCallingWithTypesRecommendation.future(
                FunctionCallingWithTypesRequest(memberId=1, gender="MALE", year="2000", command=random_command)
            )
            response = response_future.result(timeout=5)  # 5초 안에 응답 대기

            # 응답이 성공했을 때 Locust 이벤트 트리거
            self.environment.events.request.fire(
                request_type="gRPC",
                name="GetFunctionCallingWithTypesRecommendation",
                response_time=0,  # 응답 시간 (측정 가능)
                response_length=len(response.SerializeToString()),
                exception=None,
            )

        except grpc.RpcError as e:
            # gRPC 오류 발생 시 Locust 이벤트에 예외 전달
            self.environment.events.request.fire(
                request_type="gRPC",
                name="GetFunctionCallingWithTypesRecommendation",
                response_time=0,
                response_length=0,
                exception=e,
            )
            print(f"RPC Error: {e.code()} - {e.details()}")