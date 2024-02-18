import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from helper.xpath import remonline as r
from helper.data import users_data as ud
from helper.messanges import errors

driver = webdriver.Chrome()
url = 'https://web.remonline.app/login'
driver.get(url)
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_input(self, login):
        login_input_field = self.driver.find_element(By.ID, r.login_field)
        login_input_field.send_keys(login)

    def password_input(self, password):
        password_input_field = self.driver.find_element(By.ID, r.password_field)
        password_input_field.send_keys(password)

    def submit_button_click(self):
        submit_button = self.driver.find_element(By.XPATH, r.submit_button)
        submit_button.click()

    def incorrect_login_or_password(self):
        error_text = self.driver.find_element(By.XPATH, r.incorrect_login_error)
        return error_text.text


def test_error_incorrect_login_positive():
    login = LoginPage(driver)
    time.sleep(2)
    login.login_input(login=ud.user_incorrect_login)
    login.password_input(password=ud.user_incorrect_password)
    login.submit_button_click()
    time.sleep(1)
    assert login.incorrect_login_or_password() == errors.incorrect_login_or_password
