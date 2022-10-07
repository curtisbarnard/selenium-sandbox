from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Report:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.properties = self.pull_properties()

    def pull_properties(self):
        return self.boxes_section_element.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pull_titles(self):
        for property in self.properties:
            hotel_name = property.find_element(
                By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML').strip()
            print(hotel_name)
