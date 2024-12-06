from locust import HttpUser, task, between

class G123User(HttpUser):
    wait_time = between(1, 2)

    @task
    def load_game_page(self):
        self.client.get("/game/jya")

    @task
    def simulate_login(self):
        self.client.post("/login", data={"username": "test_user", "password": "password123"})
