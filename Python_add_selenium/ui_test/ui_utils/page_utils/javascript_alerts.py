from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.alert import AlertAction


class JavascriptAlerts(AlertAction):
	def __init__(self, driver: webdriver):
		super().__init__(driver)
		self.url_page = "https://the-internet.herokuapp.com/javascript_alerts"

		self._button_default_alert_xpath = "xpath=//button[text()='Click for JS Alert']"
		self._button_confirm_alert_xpath = "xpath=//button[text()='Click for JS Confirm']"
		self._button_prompt_alert_xpath = "xpath=//button[text()='Click for JS Prompt']"

		self._result_id = "id=result"

	def click_for_js_alert(self) -> str:
		self.validate_web_element(self._button_default_alert_xpath, click=True)
		self.default_alert(alert_message="I am a JS Alert")
		return self.validate_web_element(self._result_id).text

	def click_for_js_confirm(self, click_ok: bool) -> str:
		self.validate_web_element(self._button_confirm_alert_xpath, click=True)
		self.confirm_alert(click_ok=click_ok, alert_message="I am a JS Confirm")
		return self.validate_web_element(self._result_id).text

	def click_for_js_prompt(self, click_ok: bool, enter_text: str) -> str:
		self.validate_web_element(self._button_prompt_alert_xpath, clickable=True).click()
		self.prompt_alert(text=enter_text, click_ok=click_ok, alert_message="I am a JS prompt")
		return self.validate_web_element(self._result_id).text
