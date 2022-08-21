import pytest
from ui_test.ui_utils.page_utils.basic_auth import BasicAuth


@pytest.mark.usefixtures("setup")
class TestBasicAuth:
    @pytest.fixture(autouse=True)
    def setupclass(self):
        self.page_basic_auth = BasicAuth(driver=self.driver)

    def test_authentication(self):
        page_text = self.page_basic_auth.authentication()
        assert page_text == "Congratulations! You must have the proper credentials."
