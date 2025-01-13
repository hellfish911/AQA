"""This module checks html pages."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


secrets = {
    'frame1': 'Frame1_Secret',
    'frame2': 'Frame2_Secret'
}


driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")

try:

    driver.switch_to.frame('frame1')
    input1 = driver.find_element(By.ID, 'input1')
    input1.send_keys(secrets['frame1'])
    button1 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    button1.click()

    alert = Alert(driver)
    alert_text = alert.text
    assert "Верифікація пройшла успішно!" in alert_text, "Перевірка не пройдена для frame1"
    alert.accept()

    driver.switch_to.default_content()

    driver.switch_to.frame('frame2')
    input2 = driver.find_element(By.ID, 'input2')
    input2.send_keys(secrets['frame2'])
    button2 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    button2.click()

    alert = Alert(driver)
    alert_text = alert.text
    assert 'Верифікація пройшла успішно!' in alert_text, 'Перевірка не пройдена для frame2'
    alert.accept()

    print('All checks passed.')

except Exception as e:
    print(f'Error occurred: {e}')

finally:
    time.sleep(2)
    driver.quit()
