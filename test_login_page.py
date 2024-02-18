import pytest
from selenium import webdriver
from helper.pages import login as l
from helper.messanges import errors
from helper.data import users_data as ud
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    url = 'https://web.remonline.app/login'
    driver.get(url)
    yield driver
    driver.quit()

def test_error_incorrect_login_positive(browser):
    login = l.LoginPage(browser)
    time.sleep(2)
    login.login_input(login=ud.user_incorrect_login)
    login.password_input(password=ud.user_incorrect_password)
    login.submit_button_click()
    time.sleep(1)
    assert login.incorrect_login_or_password() == errors.incorrect_login_or_password
