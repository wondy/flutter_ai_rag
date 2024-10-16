import requests

class ConfluenceAPI:
    def __init__(self):
        self.base_url = "https://your-confluence-instance.atlassian.net/wiki/rest/api"
        self.auth = ("your-email@example.com", "your-api-token")

    def fetch_new_data(self):
        response = requests.get(f"{self.base_url}/content", auth=self.auth)
        response.raise_for_status()
        return response.json()
