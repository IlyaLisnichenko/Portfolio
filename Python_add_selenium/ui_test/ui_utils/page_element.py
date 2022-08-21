from typing import Union, Literal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


class PageElement:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.url_page = "https://the-internet.herokuapp.com/"

    def navigate_page(self):
        if self.driver.current_url != self.url_page:
            self.driver.get(self.url_page)
        return self

    @staticmethod
    def separation_by_and_location(value: str) -> tuple[By, str]:
        index_equals = value.find("=")
        assert index_equals != -1, f"a"

        by_str, content = value[:index_equals], value[index_equals + 1:]
        by = {
            "xpath": By.XPATH,
            "id": By.ID,
            "tag": By.TAG_NAME
        }
        assert by_str in by, f"a"

        return by[by_str], content

    def validate_web_element(self, combined_locator: str, exists: bool = True, timeout: int = 10,
                             clickable: bool = False, click: bool = False,
                             return_text: bool = False) -> Union[WebElement, str]:
        locator = self.separation_by_and_location(combined_locator)
        if exists:
            el = WebDriverWait(self.driver, timeout=timeout).until(
                ec.visibility_of_element_located(locator)
            )
            if clickable or click:
                assert el.is_enabled()
                if click:
                    el.click()
            if return_text:
                return el.text.strip()
        else:
            el = WebDriverWait(self.driver, timeout=timeout).until_not(ec.visibility_of_element_located(locator))
        return el

    def validate_all_web_elements(self, combined_locator: str, exists: bool = True, timeout: int = 10,
                                  clickable: bool = False, return_text: bool = False) -> list[Union[WebElement, str]]:
        locator = self.separation_by_and_location(combined_locator)
        if exists:
            elements = WebDriverWait(self.driver, timeout=timeout).until(ec.visibility_of_all_elements_located(locator))
            if clickable:
                for el in elements:
                    assert el.is_enabled()

            if return_text:
                return [el.text for el in elements]
        else:
            elements = WebDriverWait(self.driver, timeout=timeout).until_not(ec.visibility_of_element_located(locator))
        return elements

    def wait_web_url(self, url: str, timeout: int = 10, verification_type_url: Literal['CHANGES', 'TO_BE'] = 'CHANGES'):
        WebDriverWait(self.driver, timeout=timeout).until(
            ec.url_changes(url) if verification_type_url == 'CHANGES' else ec.url_to_be(url)
        )
        return self

    def checkbox(self, combined_locator: str, select_checkbox: bool) -> WebElement:
        element_checkbox = self.validate_web_element(combined_locator, clickable=True)
        assert element_checkbox.get_attribute("type") == "checkbox", "Element is not a checkbox, use other method"

        good_condition_in_checkbox = ec.element_selection_state_to_be(element_checkbox, select_checkbox)
        if not good_condition_in_checkbox(self.driver):
            element_checkbox.click()
            assert good_condition_in_checkbox(self.driver), "Checkbox is not active"

        return element_checkbox

    def dropdown(self, value: Union[str, int], combined_locator: str,
                 by_value_or_text: Literal["value", "text"] = "value") -> str:
        select_object = Select(self.validate_web_element(combined_locator=combined_locator))

        if by_value_or_text == "value":
            select_object.select_by_value(str(value))
        else:
            select_object.select_by_visible_text(str(value))
        return select_object.first_selected_option.text

    def input_web_element(self, combined_locator: str, value: Union[str, int] = None):
        input_element = self.validate_web_element(combined_locator=combined_locator, clickable=True)
        if value is not None:
            input_element.clear()
            input_element.send_keys(value)
        return input_element
