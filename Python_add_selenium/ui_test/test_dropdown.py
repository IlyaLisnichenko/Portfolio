import pytest
from ui_test.ui_utils.page_utils.dropdown import Dropdown


@pytest.mark.usefixtures("setup")
class TestDropdown:
    @pytest.fixture(autouse=True)
    def setupclass(self):
        self.page_dropdown = Dropdown(driver=self.driver)
        self.page_dropdown.navigate_page()

    @pytest.mark.parametrize(
        "value, option_text",
        [
            (1, "Option 1"),
            (2, "Option 2")
        ]
    )
    def test_dropdown_value(self, value, option_text):
        result = self.page_dropdown.dropdown_list(value=value)
        assert result == option_text

    @pytest.mark.parametrize(
        "option_text",
        ["Option 1", "Option 2"]
    )
    def test_dropdown_text(self, option_text):
        result = self.page_dropdown.dropdown_list(value=option_text, by_value_or_text="text")
        assert result == option_text
