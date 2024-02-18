from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://google.com'
driver.get(url)

time.sleep(3)