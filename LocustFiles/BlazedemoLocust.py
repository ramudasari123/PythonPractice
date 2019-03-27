from locust import Locust, TaskSet, task

class Loginblazedemo(TaskSet):
    @task(1)
    def Launch(self):
        self.client.get("/")
    @task(2)
    def Login(self):
        self.client.post("/login",{'email': 'LocustPerformanceUser1@gmail.com', 'password': '123456'})
    @task(3)
    def SelectFlight(self):
        self.client.post("/reserve.php",{'fromPort':'','toPort':''})

class LoginUniqueUserTest(Locust):
    task_set = Loginblazedemo
    host = "http://blazedemo.com"
    sock=None