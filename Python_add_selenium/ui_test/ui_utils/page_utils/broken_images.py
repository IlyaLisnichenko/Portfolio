from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.exception_error.broker_images_exception import BrokenImagesException
from ui_test.ui_utils.page_element import PageElement
from conftest import main_url
import requests


class BrokenImages(PageElement):
	def __init__(self, driver: webdriver):
		super().__init__(driver)
		self.url_page = "https://the-internet.herokuapp.com/broken_images"
		self._content_page = "id=content"
		self._img_xpath = "xpath=//div[@id='content']//img"
		self._error_img = "Status code img - [{}]\n" \
						  "url image - [{}]\n\n"

	def validate_images_in_page(self):
		img_elements = self.validate_all_web_elements(self._img_xpath)

		count_broken_img = 0
		error_info = ""
		for img in img_elements:
			url_img = img.get_attribute("src")

			res = requests.get(url_img)
			if res.status_code != 200:
				count_broken_img += 1
				error_info += self._error_img.format(res.status_code, url_img)

		if error_info:
			error = f"url_page - [{self.url_page}]\n" \
					f"Broken Images - {count_broken_img}/{len(img_elements)}\n"
			raise BrokenImagesException(error + error_info)
		return self
