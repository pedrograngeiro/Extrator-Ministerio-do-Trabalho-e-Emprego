# Importações
import requests

class RequestFactory:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def create_post_request(self, data):
        response = requests.post(self.url, headers=self.headers, data=data)
        return response