from typing import Literal
from selenium.webdriver.support.color import Color
from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.page_element import PageElement


class Login(PageElement):
	def __init__(self, driver: webdriver):
		super().__init__(driver)
		self.url_page = "https://the-internet.herokuapp.com/login"

		self._user_name_id = "id=username"
		self._password_id = "id=password"

		self._button_login_tag = "tag=button"
		self._button_logout_xpath = "xpath=//a[@class='button secondary radius']"

		self._message_id = "id=flash"
		self._secure_area_url_contein = "/secure"

		self._color_red = Color.from_string('rgb(198, 15, 19)')
		self._color_green = Color.from_string('rgb(93, 164, 35)')

		self._successful_message_login = "You logged into a secure area!"
		self._successful_message_logout = "You logged out of the secure area!"

	def login(self, user_name: str = None, password: str = None, message_error: str = None):
		self.input_web_element(combined_locator=self._user_name_id, value=user_name)
		self.input_web_element(combined_locator=self._password_id, value=password)

		self.validate_web_element(combined_locator=self._button_login_tag, click=True)
		if message_error is not None:
			self._validate_authorization_message(expect_message=message_error)
		else:
			self._validate_authorization_message(expect_message=self._successful_message_login, action="LOGIN")
		return self

	def logout(self):
		self.wait_web_url(url=self._secure_area_url_contein)
		self.validate_web_element(combined_locator=self._button_logout_xpath, click=True)

		self._validate_authorization_message(expect_message=self._successful_message_logout, action="LOGOUT")
		return self

	def _validate_authorization_message(self, expect_message: str, action: Literal['LOGIN', 'LOGOUT'] = None):
		if action == 'LOGIN':
			self.wait_web_url(url=self._secure_area_url_contein)
		elif action in ('LOGOUT', None):
			self.wait_web_url(url=self.url_page, verification_type_url="TO_BE")

		notice_element = self.validate_web_element(combined_locator=self._message_id)
		notice_text = self.validate_web_element(combined_locator=self._message_id).text.strip().rstrip("\n×")
		notice_colour = Color.from_string(notice_element.value_of_css_property('background-color'))

		def validate_text_and_color(expect_color):
			assert notice_colour == expect_color, \
				f"Expect notice color [rgba - {expect_color}, hex - {expect_color.hex}]\n " \
				f"Actual notice color [rgba - {notice_colour}, hex - {notice_colour.hex}]"
			assert notice_text == expect_message, \
				f"Expected notice text - {expect_message}\n " \
				f"Alert notice text- {notice_text}"

		if action == 'LOGIN':
			validate_text_and_color(self._color_green)
		elif action == 'LOGOUT':
			validate_text_and_color(self._color_green)
		else:
			validate_text_and_color(self._color_red)
		return self
