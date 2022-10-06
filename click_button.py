import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:/Users/Curtis/Documents/seleniumdrivers"

driver = webdriver.Chrome()
driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')

# Waits just in case the browser is slow, will only wait until that element is found. This only needs to be called once per session and will apply to all elements
driver.implicitly_wait(3)

# Finding a button on the page and clicking it
download_button = driver.find_element(By.ID, 'downloadButton')
download_button.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), 'Complete!'
    )
)
