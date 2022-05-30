from random_generate import random_str, random_int
from datetime import date, timedelta
from config import data_format
import random


today = date.today()


class Booking:
    def __init__(self):
        self.firstname = random_str(6)
        self.lastname = random_str(6)
        self.totalprice = int(random_int())
        self.depositpaid = random.choice([True, False])
        self.checkin = today - timedelta(days=random.randrange(5, 30))
        self.checkout = today
        self.additionalneeds = random_str()

    def convert_in_dict(self, return_params: list = None) -> dict:
        data = self.__dict__.copy()
        return_params = set(return_params) if isinstance(return_params, list) else return_params
        attributes = data.keys()
        assert return_params is None or return_params <= attributes, "help"

        return_params = return_params or attributes
        bookingdates = dict()
        for attribute, value in data.copy().items():
            if attribute in return_params:
                if isinstance(value, date):
                    bookingdates.setdefault("bookingdates", dict()).update({attribute: value.strftime(data_format)})
                    data.pop(attribute)
            else:
                data.pop(attribute)
        data.update(bookingdates)
        return data
