from locust import HttpUser, task, between, TaskSet
import pymysql

class tagRecommendTest(TaskSet):
    @task
    def getSongsNew(self):
        if not hasattr(self.user, "headers"):
            print("ERROR: Headers not set!")
            return
        
        self.client.get("/api/v1/songs/new", headers=self.user.headers)
    
    # @task
    # def tagRecommendV2Refresh(self):
    #     self.client.post("/api/v2/recommend/refresh")

    # @task
    # def getRecentSearch(self):
    #     self.client.get("/api/v1/recent/search")


class LocustUser(HttpUser):
    host = "https://www.singsongsangsong.life"
    tasks = [tagRecommendTest]
    wait_time= between(1,3)

    def on_start(self):
        response = self.client.post("/api/v2/member/login", 
                        json={
                            "deviceToken": "string",
                            "idToken": "string",
                            "provider": "Anonymous"
                        })
        
        # JSON 응답 변환
        response_json = response.json()  # response를 JSON 형태로 변환

        # 응답 데이터가 올바르게 들어왔는지 확인
        if "data" in response_json and "accessToken" in response_json["data"]:
            self.token = response_json["data"]["accessToken"]
            self.headers = {
                "Authorization": f"Bearer {self.token}",
                'accept': 'application/json'
            }
        else:
            print("ERROR: Unexpected response format:", response_json)
