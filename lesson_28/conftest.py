import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://guest:welcome2qauto@qauto2.forstudy.space/')
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    print('Initializing LoginPage fixture')
    from .pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture
def registration_page(driver):
    from .pages.registration_page import RegistrationPage
    return RegistrationPage(driver)
