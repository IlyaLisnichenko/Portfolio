import pytest
from ui_test.ui_utils.page_utils.login import Login
from ui_utils.random_str import random_str
from login_access import user_name_login, password_login


@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setupclass(self):
        self.page_login = Login(driver=self.driver)
        self.page_login.navigate_page()

    @pytest.mark.parametrize(
        "user_name, password, message",
        [
            (None, None, "Your username is invalid!"),
            (None, random_str(), "Your username is invalid!"),
            (None, password_login, "Your username is invalid!"),
            (random_str(), random_str(), "Your username is invalid!"),
            (random_str(), password_login, "Your username is invalid!"),
            (random_str(), None, "Your username is invalid!"),
            (user_name_login, None, "Your password is invalid!"),
            (user_name_login, random_str(), "Your password is invalid!")
        ]
    )
    def test_negative_login(self, user_name, password, message):
        self.page_login.login(user_name=user_name, password=password, message_error=message)

    def test_positive_login(self):
        self.page_login.login(user_name=user_name_login, password=password_login)

    def test_logout(self):
        self.page_login.login(user_name=user_name_login, password=password_login)
        self.page_login.logout()
