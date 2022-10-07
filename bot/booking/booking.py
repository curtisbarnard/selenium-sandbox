from random import randint
from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

import booking.constants as const
from booking.filters import Filters


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/Users/Curtis/Documents/seleniumdrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        sleep(randint(1, 2))
        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()

        sleep(randint(2, 5))

        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_guest(self, num_of_adults):
        toggle = self.find_element(By.ID, "xp__guests__toggle")
        toggle.click()
        adult_val_el = self.find_element(
            By.ID, 'group_adults')
        adult_count = int(adult_val_el.get_attribute('value'))

        while adult_count > num_of_adults:
            print(adult_count)
            decr = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
            sleep(randint(1, 2))
            decr.click()
            adult_count = int(adult_val_el.get_attribute('value'))
            print(adult_count)

        while adult_count < num_of_adults:
            print(adult_count)
            incr = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
            sleep(randint(1, 2))
            incr.click()
            adult_count = int(adult_val_el.get_attribute('value'))
            print(adult_count)

    def search(self):
        search_button = self.find_element(
            By.CLASS_NAME, "sb-searchbox__button")
        search_button.click()

    def apply_filters(self):
        filter = Filters(driver=self)
        filter.apply_star_rating(4, 5)
        sleep(randint(2, 4))
        filter.sort_by_lowest_price()
