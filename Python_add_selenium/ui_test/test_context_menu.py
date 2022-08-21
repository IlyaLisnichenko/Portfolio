import pytest
import random
from ui_test.ui_utils.page_utils.context_menu import ContextMenu


@pytest.mark.usefixtures("setup")
class TestContextMenu:
    @pytest.fixture(autouse=True)
    def setupclass(self):
        self.page_context_menu = ContextMenu(driver=self.driver)
        self.page_context_menu.navigate_page()

    def test_click_blue_button(self):
        self.page_context_menu.context_click()




