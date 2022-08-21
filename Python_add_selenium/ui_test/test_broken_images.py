import pytest
from ui_test.ui_utils.page_utils.broken_images import BrokenImages
from ui_test.ui_utils.exception_error.broker_images_exception import BrokenImagesException


@pytest.mark.usefixtures("setup")
class TestBrokenImages:
    def test_broken_images_2_of_3(self):
        self.page_broken_images = BrokenImages(self.driver)
        self.page_broken_images.navigate_page()

        with pytest.raises(BrokenImagesException, match=r"Broken Images - 2/3"):
            self.page_broken_images.validate_images_in_page()
