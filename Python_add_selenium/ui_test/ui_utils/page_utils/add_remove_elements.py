from selenium.common import TimeoutException
from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.page_element import PageElement
import random


class AddRemoveElement(PageElement):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.url_page = "https://the-internet.herokuapp.com/add_remove_elements/"
        self._button_add_element = "xpath=//button[text()='Add Element']"
        self._button_delete = "xpath=//button[text()='Delete']"

    def add_element(self, count_click: int = 1) -> int:
        assert count_click >= 0, f"Count click must be more [0], your count click - [{count_click}]"
        if count_click == 0:
            return 0

        for click in range(count_click):
            self.validate_web_element(self._button_add_element, click=True)
        return self._count_delete_element()

    def delete_element(self, count_click: int = 1) -> int:
        assert count_click >= 0, f"Count click must be more [0], your count click - [{count_click}]"
        if count_click == 0:
            return 0

        for click in range(count_click):
            delete_button = self.validate_all_web_elements(self._button_delete, clickable=True)
            random.choice(delete_button).click()

        return self._count_delete_element()

    def _count_delete_element(self) -> int:
        try:
            elements = self.validate_all_web_elements(self._button_delete, clickable=True, timeout=1)
            return len(elements)
        except TimeoutException:
            self.validate_web_element(self._button_delete, exists=False)
            return 0
