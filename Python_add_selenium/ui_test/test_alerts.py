import pytest
from ui_test.ui_utils.page_utils.javascript_alerts import JavascriptAlerts
from ui_test.ui_utils.random_str import random_str

random_str = random_str()


@pytest.mark.usefixtures("setup")
class TestContextMenu:
    @pytest.fixture(autouse=True)
    def setupclass(self):
        self.page_javascript_alerts = JavascriptAlerts(driver=self.driver)
        self.page_javascript_alerts.navigate_page()

    def test_click_for_js_alert(self):
        result_str = self.page_javascript_alerts.click_for_js_alert()
        assert result_str == "You successfully clicked an alert"

    @pytest.mark.parametrize("click_ok", [True, False])
    def test_click_for_js_confirm(self, click_ok):
        result_str = self.page_javascript_alerts.click_for_js_confirm(click_ok=click_ok)
        expected_result = "You clicked: Ok" if click_ok else "You clicked: Cancel"
        assert result_str == expected_result

    @pytest.mark.parametrize(
        "click_ok, text, result",
        [
            (True, None, "You entered:"),
            (False, None, "You entered: null"),
            (True, random_str, f"You entered: {random_str}"),
            (False, random_str, "You entered: null")
         ]
    )
    def test_click_for_js_prompt(self, click_ok, text, result):
        result_str = self.page_javascript_alerts.click_for_js_prompt(click_ok=click_ok, enter_text=text)
        assert result_str == result




