import pytest
import random
from ui_test.ui_utils.page_utils.challenging_dom import ChallengingDom


@pytest.mark.usefixtures("setup")
class TestChallengingDom:
    @pytest.fixture(autouse=True)
    def setupclass(self):
        self.page_challenging_dom = ChallengingDom(driver=self.driver)
        self.page_challenging_dom.navigate_page()

    def test_click_blue_button(self):
        assert self.page_challenging_dom.click_blue_button()

    def test_click_red_button(self):
        assert self.page_challenging_dom.click_red_button()

    def test_click_green_button(self):
        assert self.page_challenging_dom.click_green_button()

    def test_edit_line_in_table(self):
        ip_sum = f"Apeirian{random.randrange(0, 9)}"
        assert self.page_challenging_dom.edit_line_in_table(ip_sum=ip_sum)

    def test_delete_line_in_table(self):
        ip_sum = f"Apeirian{random.randrange(0, 9)}"
        assert self.page_challenging_dom.delete_line_in_table(ip_sum=ip_sum)


