import pytest
from ui_test.ui_utils.page_utils.drag_and_drop import DragAndDrop


@pytest.mark.usefixtures("setup")
class TestDragAndDrop:
    @pytest.fixture(autouse=True)
    def setupclass(self):
        self.page_drag_and_drop = DragAndDrop(driver=self.driver)
        self.page_drag_and_drop.navigate_page()

    @pytest.mark.parametrize(
        "block_deviation, expect_condition",
        [
            (None, True),
            ("LEFT", False),
            ("RIGHT", False),
            ("TOP", False),
            ("BOTTOM", False)
        ]
    )
    def test_drag_a_and_drop_in_b(self, block_deviation, expect_condition):
        elements_have_changed = self.page_drag_and_drop.drag_and_drop_element(block_deviation=block_deviation)
        assert elements_have_changed == expect_condition
