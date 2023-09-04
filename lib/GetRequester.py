import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = self.url
        response = requests.get(URL)
        return response.content

    def load_json(self):

        response_text = self.get_response_body()
        response_data = json.loads(response_text)  # Parse JSON data from the response text
        return response_data
