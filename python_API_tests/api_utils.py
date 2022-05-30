import requests
from config import booker_url, username, password


class API:
    def __init__(self):
        self._url_booking = booker_url + "booking"
        self._url_ping = booker_url + "ping"
        self._url_auth = booker_url + "auth"

    def connect_ping(self, status_cod: int):
        return self._requests_api(url=self._url_ping, method="GET", status_cod=status_cod)

    def create_token(self) -> dict:
        auth = {
            "username": username,
            "password": password
        }

        return self._requests_api(url=self._url_auth, method="POST", status_cod=200, data=auth)

    def booking(self, method: str, status_cod: int,
                params: dict = None, booking_id: int = None,
                json: dict = None, token: str = None, data: dict = None):

        url = self._url_booking if booking_id is None else f"{self._url_booking}/{booking_id}"
        token = dict(token=token) if token is not None else None

        return self._requests_api(
            url=url, method=method, status_cod=status_cod,
            params=params, json=json, cookies=token, data=data
        )

    @staticmethod
    def _requests_api(url: str, method: str, status_cod: int,
                      data: dict = None, params: dict = None, json: dict = None, cookies: dict = None):
        requests_method = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "PATCH": requests.patch,
            "DELETE": requests.delete,
        }
        assert method in requests_method, f"method should be [{requests_method.keys()}] your method is [{method}]"

        response = requests_method[method](url, data=data, params=params, json=json, cookies=cookies)
        assert response.status_code == status_cod, \
            f"Expected status cod - [{status_cod}], actual status cod - [{response.status_code}]"

        return response.json() if 'application/json' in response.headers["Content-Type"] else response.text
