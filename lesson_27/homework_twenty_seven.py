"""This module verifies tracking number."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class NovaPoshtaTracker:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://tracking.novaposhta.ua/#/uk'

    def open_page(self):
        """Open NP page."""
        self.driver.get(self.url)

    def enter_tracking_number(self, tracking_number):
        """Enter number into the field."""
        tracking_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'en'))
        )
        tracking_input.clear()
        tracking_input.send_keys(tracking_number)
        tracking_input.send_keys(Keys.RETURN)

    def get_parcel_status(self):
        """Get status"""

        status_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(), 'Ми не знайшли посилку')]")
            )
        )
        return status_element.text


@pytest.fixture
def driver():
    """WebDriver setup fixture"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_negative_status(driver):
    """Verify given track number"""
    tracker = NovaPoshtaTracker(driver)
    tracking_number = '20450062606102'
    expected_status = ('Ми не знайшли посилку за таким номером. '
                       'Якщо ви шукаєте інформацію про посилку, якій більше 3 місяців, '
                       'будь ласка, зверніться у контакт-центр: 0 800 500 609')

    tracker.open_page()
    tracker.enter_tracking_number(tracking_number)
    actual_status = tracker.get_parcel_status()

    assert actual_status == expected_status, f"Очікувався статус '{expected_status}', але отримано '{actual_status}'."
