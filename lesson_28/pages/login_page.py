"""This module logins user."""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-target='#signin']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")

    def go_to_registration(self):
        self.click_element(*self.REGISTER_BUTTON)
