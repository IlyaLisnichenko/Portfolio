from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.action_mouse import ActionMouse
from ui_test.ui_utils.alert import AlertAction


class ContextMenu(ActionMouse, AlertAction):
	def __init__(self, driver: webdriver):
		super().__init__(driver)
		self.url_page = "https://the-internet.herokuapp.com/context_menu"

		self._context_menu_id = "id=hot-spot"

	#TODO: дороботать и причесать

	def context_click(self):
		self.context_click_for_element(self._context_menu_id)
		self.default_alert(alert_message="You selected a context menu")
