from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.page_element import PageElement
from typing import Literal


class ChallengingDom(PageElement):
	def __init__(self, driver: webdriver):
		super().__init__(driver)
		self.url_page = "https://the-internet.herokuapp.com/challenging_dom"

		self._blue_button_xpath = "xpath=//a[@class='button']"
		self._red_button_xpath = "xpath=//a[@class='button alert']"
		self._green_button_xpath = "xpath=//a[@class='button success']"
		self._all_button_xpath = "xpath=//a[contains(@class, 'button')]"

		self._action_xpath = "xpath=//tr[td[2][text()='{ip_sum}']]//a[text()='{action}']"

	def click_blue_button(self) -> bool:
		return self._challenging_button(self._blue_button_xpath)

	def click_red_button(self) -> bool:
		return self._challenging_button(self._red_button_xpath)

	def click_green_button(self) -> bool:
		return self._challenging_button(self._green_button_xpath)

	def edit_line_in_table(self, ip_sum: str) -> bool:
		return self._action_with_line_in_table(ip_sum=ip_sum, action="edit")

	def delete_line_in_table(self, ip_sum: str) -> bool:
		return self._action_with_line_in_table(ip_sum=ip_sum, action="delete")

	def _action_with_line_in_table(self, ip_sum: str, action: Literal['edit', 'delete']) -> bool:
		self.validate_web_element(
			self._action_xpath.format(
				ip_sum=ip_sum,
				action=action
			),
			click=True
		)
		# action button click marker
		return self.driver.current_url == self.url_page + f"#{action}"

	def _challenging_button(self, combined_locator: str) -> bool:
		old_text_button = self.validate_all_web_elements(self._all_button_xpath, return_text=True)
		self.validate_web_element(combined_locator, click=True)
		new_text_button = self.validate_all_web_elements(self._all_button_xpath, return_text=True)
		return old_text_button != new_text_button

