from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote.webelement import WebElement
from ui_test.ui_utils.page_element import PageElement


class ActionMouse(PageElement):
    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def context_click_for_element(self, location: str):
        element = self.validate_web_element(combined_locator=location)
        ActionChains(self.driver).context_click(element).perform()
        return self

    def drag_and_drop(self, draggable_element: WebElement, droppable_element: WebElement,
                      by_offset: tuple[int, int] = None):
        if by_offset:
            ActionChains(self.driver)\
                .click_and_hold(draggable_element)\
                .move_to_element_with_offset(droppable_element, by_offset[0], by_offset[1])\
                .release() \
                .perform()
        else:
            ActionChains(self.driver).drag_and_drop(draggable_element, droppable_element).perform()
        return self
