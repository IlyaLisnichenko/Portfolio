import pytest
import random
from ui_test.ui_utils.page_utils.add_remove_elements import AddRemoveElement


random_int = random.randrange(3, 7)


@pytest.mark.usefixtures("setup")
class TestAddRemoveElement:
    @pytest.fixture(autouse=True)
    def setupclass(self):
        self.add_remove_element = AddRemoveElement(driver=self.driver)
        self.add_remove_element.navigate_page()
        yield self
        self.driver.refresh()

    def test_add_element(self):
        assert self.add_remove_element.add_element() == 1

    @pytest.mark.parametrize("add_element, delete_element", [(random_int, 1), (random_int, random_int)])
    def test_add_and_delete_elements(self, add_element, delete_element):
        assert self.add_remove_element.add_element(count_click=add_element) == add_element
        assert self.add_remove_element.delete_element(count_click=delete_element) == add_element - delete_element



