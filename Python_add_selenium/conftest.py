from selenium import webdriver
import pytest


main_url = "https://the-internet.herokuapp.com/"


@pytest.fixture(scope="class")
def init_chrome_driver():
    driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
    return driver


@pytest.fixture(scope="class")
def setup(request, init_chrome_driver):
    driver = init_chrome_driver
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(main_url)
    yield driver
    driver.close()
    driver.quit()
