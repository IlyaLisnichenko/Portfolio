import pytest
from ui_test.ui_utils.page_utils.checkboxes import Checkboxes


@pytest.mark.usefixtures("setup")
class TestCheckboxes:
    @pytest.fixture(autouse=True)
    def setupclass(self):
        self.page_checkboxes = Checkboxes(driver=self.driver)
        self.page_checkboxes.navigate_page()

    @pytest.mark.parametrize(
        "checkbox_1, checkbox_2",
        [
            (False, False),
            (False, True),
            (True, False),
            (True, True)
        ]
    )
    def test_add_and_delete_elements(self, checkbox_1, checkbox_2):
        assert self.page_checkboxes.activation_checkbox(
            checkbox_1=checkbox_1, checkbox_2=checkbox_2
        ) == (checkbox_1, checkbox_2)
