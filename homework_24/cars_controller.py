
import requests
from requests.auth import HTTPBasicAuth


class CarsController:
    BASE_URL = "http://127.0.0.1:8080"

    def __init__(self):
        self.session = requests.Session()

    def login(self, username, password):
        return self.session.post(
            f"{self.BASE_URL}/auth",
            auth=HTTPBasicAuth(username, password)
        )

    def get_cars(self, limit=None, sort_by=None, token=None):
        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        params = {}

        if limit is not None:
            params["limit"] = limit

        if sort_by is not None:
            params["sort_by"] = sort_by

        return self.session.get(
            f"{self.BASE_URL}/cars",
            params=params,
            headers=headers
        )
