"""This module contains Base Page class."""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click_element(self, by, locator):
        self.find_element(by, locator).click()

    def input_text(self, by, locator, text):
        element = self.find_element(by, locator)
        element.clear()
        element.send_keys(text)
