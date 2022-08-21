import requests
from bs4 import BeautifulSoup


def create_py_file():
    url = "https://the-internet.herokuapp.com"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    for li in soup.find_all("li"):
        part_link = li.find("a").get("href")
        link = url + part_link
        file_mame = part_link.strip('/').replace("/", "_")
        if file_mame == "add_remove_elements":
            continue

        class_name = file_mame.title().replace("_", "")
        with open(f"E:\\Portfolio\\Python_add_selenium\\ui_test\\ui_utils\\page_utils\\{file_mame}.py", "w") as file:
            file.write(
                'from selenium.webdriver.chrome import webdriver\n'
                'from ui_test.ui_utils.page_element import PageElement\n\n\n'
                f'class {class_name}(PageElement):\n'
                '\tdef __init__(self, driver: webdriver):\n'
                '\t\tsuper().__init__(driver)\n'
                f'\t\tself.url_page = "{link}"\n'
            )


if __name__ == '__main__':
    create_py_file()
