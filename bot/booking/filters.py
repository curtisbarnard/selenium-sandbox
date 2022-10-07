# Bring in WebDriver for typing
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Filters:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filter_box = self.driver.find_element(
            By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        star_child_elements = star_filter_box.find_elements(
            By.CSS_SELECTOR, '*')

        for star_value in star_values:
            for element in star_child_elements:
                if element.get_attribute('data-filters-item') == f'class:class={star_value}':
                    check_box = element.find_element(
                        By.CLASS_NAME, 'bbdb949247')
                    check_box.click()
