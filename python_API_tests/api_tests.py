from datetime import date, timedelta
from book_model import Booking
from api_utils import API
from random_generate import random_str
import random

booking = Booking()
api = API()

token: str
booking_id: int


class TestIssueRefactored:
    @staticmethod
    def test_00_health_check():
        response = api.connect_ping(status_cod=201)
        assert response == 'Created'

    @staticmethod
    def test_01_create_token():
        global token

        response = api.create_token()
        assert "token" in response.keys()
        token = response["token"]

    @staticmethod
    def test_02_create_booking():
        global booking_id
        new_booking = booking.convert_in_dict()

        response = api.booking(method="POST", status_cod=200, json=new_booking)
        assert response["booking"] == new_booking
        booking_id = response["bookingid"]

    @staticmethod
    def test_03_get_booking_ids():
        today = date.today()
        old_month_data = today - timedelta(days=random.randrange(30, 60))
        params = {
            "checkin": old_month_data,
            "checkout": today
        }

        response = api.booking(method="GET", status_cod=200, params=params)
        assert len(response) != 0

    @staticmethod
    def test_04_get_booking():
        response = api.booking(method="GET", status_cod=200, booking_id=booking_id)
        assert response == booking.convert_in_dict()

    @staticmethod
    def test_05_update_booking():
        global booking
        booking = Booking()
        new_booking = booking.convert_in_dict()

        response = api.booking(method="PUT", status_cod=200, booking_id=booking_id, json=new_booking, token=token)
        assert response == new_booking

    @staticmethod
    def test_06_partial_update_booking():
        booking.lastname = random_str()
        booking.firstname = random_str()
        partial_booking = booking.convert_in_dict(["lastname", "firstname"])

        response = api.booking(method="PATCH", status_cod=200, booking_id=booking_id, json=partial_booking, token=token)
        assert response == booking.convert_in_dict()

    @staticmethod
    def test_07_delete_booking():
        response = api.booking(method="DELETE", status_cod=201, booking_id=booking_id, token=token)
        assert response == 'Created'

    @staticmethod
    def test_08_get_delete_booking():
        response = api.booking(method="GET", status_cod=404, booking_id=booking_id)
        assert response == "Not Found"
