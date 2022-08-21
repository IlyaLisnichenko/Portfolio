from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.page_element import PageElement


class Upload(PageElement):
	def __init__(self, driver: webdriver):
		super().__init__(driver)
		self.url_page = "https://the-internet.herokuapp.com/upload"
