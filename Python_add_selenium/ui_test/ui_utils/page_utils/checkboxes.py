from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.page_element import PageElement


class Checkboxes(PageElement):
	def __init__(self, driver: webdriver):
		super().__init__(driver)
		self.url_page = "https://the-internet.herokuapp.com/checkboxes"
		self._checkbox_xpath = "xpath=//input[{index_element}]"

	def activation_checkbox(self, checkbox_1: bool = False, checkbox_2: bool = False) -> tuple[bool, bool]:
		element_checkbox_1 = self.checkbox(self._checkbox_xpath.format(index_element=1), select_checkbox=checkbox_1)
		element_checkbox_2 = self.checkbox(self._checkbox_xpath.format(index_element=2), select_checkbox=checkbox_2)
		return element_checkbox_1.is_selected(), element_checkbox_2.is_selected()
