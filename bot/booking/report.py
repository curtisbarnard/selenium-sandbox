from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Report:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.properties = self.pull_properties()

    def pull_properties(self):
        return self.boxes_section_element.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pull_property_attributes(self):
        collection = []
        for property in self.properties:
            hotel_name = property.find_element(
                By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML').strip()

            hotel_price = '$0'
            hotel_price_el = property.find_elements(
                By.CSS_SELECTOR, 'span[class~="bd73d13072"]')

            if (len(hotel_price_el) == 0):
                hotel_price_el = property.find_elements(
                    By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]')

            if (len(hotel_price_el) > 0):
                hotel_price = hotel_price_el[0].get_attribute(
                    'innerHTML').strip()

            hotel_score = property.find_element(
                By.CSS_SELECTOR, 'div[aria-label*="Scored"]').get_attribute('innerHTML').strip()

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )

        return collection
