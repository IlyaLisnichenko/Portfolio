from selenium.webdriver.chrome import webdriver
from ui_test.ui_utils.page_element import PageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert


class AlertAction(PageElement):
    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def default_alert(self, alert_message: str = None, timeout: int = 10):
        alert = self._wait_alert(timeout=timeout)

        self._validate_alert_message(alert, alert_message=alert_message)
        self._action_alert(alert)

        self._wait_alert(timeout=timeout, exists=False)
        return self

    def confirm_alert(self, alert_message: str = None, timeout: int = 10, click_ok: bool = True):
        self._wait_alert(timeout=timeout)
        alert = self.driver.switch_to.alert

        self._validate_alert_message(alert, alert_message=alert_message)
        self._action_alert(alert, click_ok=click_ok)

        self._wait_alert(timeout=timeout, exists=False)
        return self

    def prompt_alert(self, text: str = None, alert_message: str = None, timeout: int = 10, click_ok: bool = True):
        self._wait_alert(timeout=timeout)
        alert = Alert(self.driver)
        if text is not None:
            alert.send_keys(text)
        self._validate_alert_message(alert, alert_message=alert_message)
        self._action_alert(alert, click_ok=click_ok)

        self._wait_alert(timeout=timeout, exists=False)
        return self

    def _action_alert(self, alert: Alert, click_ok: bool = True):
        if click_ok:
            alert.accept()
        else:
            alert.dismiss()
        return self

    def _validate_alert_message(self, alert: Alert, alert_message: str = None):
        alert_text = alert.text
        if alert_message is not None:
            assert alert_text == alert_message, f"Alert text does not match expected\n " \
                                                f"Alert_text- {alert_text}\n " \
                                                f"Expected alert text - {alert_message}"
        return self

    def _wait_alert(self, timeout: int = 10, exists: bool = True) -> Alert:
        if exists:
            alert = WebDriverWait(self.driver, timeout=timeout).until(ec.alert_is_present())
        else:
            alert = WebDriverWait(self.driver, timeout=timeout).until_not(ec.alert_is_present())
        return alert

