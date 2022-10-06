import os
from selenium import webdriver
from selenium.webdriver.common.by import By
# Brings in the ability to "press" keyboard keys
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:/Users/Curtis/Documents/seleniumdrivers"

driver = webdriver.Chrome()

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
driver.implicitly_wait(5)

value_a = driver.find_element(By.ID, "sum1")
value_b = driver.find_element(By.ID, "sum2")

value_a.send_keys(Keys.NUMPAD2, Keys.NUMPAD1)
value_b.send_keys(Keys.NUMPAD6)

btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btn.click()
