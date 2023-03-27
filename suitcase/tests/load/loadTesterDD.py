from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    def on_start(self):
        self.client.verify = False

    @task
    def td(self):
        self.client.get("/acg:lab:suitcase-dd/")
        
    @task
    def getProperty(self):
        self.client.get("/acg:lab:suitcase-dd/property/luminosity-dimmer1/")