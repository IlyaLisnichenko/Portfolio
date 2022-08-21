from typing import Literal, Union
from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.page_element import PageElement


class Dropdown(PageElement):
	def __init__(self, driver: webdriver):
		super().__init__(driver)
		self.url_page = "https://the-internet.herokuapp.com/dropdown"
		self._dropdown_id = "id=dropdown"
		
	def dropdown_list(self, value: Union[str, int], by_value_or_text: Literal["value", "text"] = "value") -> str:
		return self.dropdown(value=value, by_value_or_text=by_value_or_text, combined_locator=self._dropdown_id)
