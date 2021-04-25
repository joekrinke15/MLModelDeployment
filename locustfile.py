from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(10, 15)
    
    @task
    def index(self):
        self.client.post("/result", json = 
                         {
                             "age": 23,
                             "bmi": 25, 
                             "children": 2, 
                             "female":0, 
                             "male":1, 
                             "no":1, 
                             "yes":0, 
                             "northeast":1, 
                             "northwest":0, 
                             "southeast":0, 
                             "southwest":0
                         }
                        )