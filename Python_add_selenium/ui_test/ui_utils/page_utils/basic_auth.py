from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.alert import AlertAction
from login_access import user_name, password


class BasicAuth(AlertAction):
	def __init__(self, driver: webdriver):
		super().__init__(driver)
		self.url_page = f"https://{user_name}:{password}@the-internet.herokuapp.com/basic_auth"

		self._page_text_tag = "tag=p"

	def authentication(self) -> str:
		self.navigate_page()
		return self.validate_web_element(combined_locator=self._page_text_tag, return_text=True)
