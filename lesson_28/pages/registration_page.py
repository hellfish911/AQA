"""This module  should register user."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage


class RegistrationPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'signupName')
    LAST_NAME_INPUT = (By.ID, 'signupLastName')
    EMAIL_INPUT = (By.ID, 'signupEmail')
    PASSWORD_INPUT = (By.ID, 'signupPassword')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'signupRepeatPassword')
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Register']")
    GARAGE_HEADER = (By.XPATH, "//h1[normalize-space(text())='Garage']")

    def register_user(self, first_name, last_name, email, password):
        self.input_text(*self.FIRST_NAME_INPUT, first_name)
        self.input_text(*self.LAST_NAME_INPUT, last_name)
        self.input_text(*self.EMAIL_INPUT, email)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.input_text(*self.CONFIRM_PASSWORD_INPUT, password)
        self.click_element(*self.SUBMIT_BUTTON)

    def is_garage_page_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.GARAGE_HEADER)
            )
            return True
        except TimeoutException:
            return False
