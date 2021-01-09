from selenium.webdriver.common.by import By
from .base_element import BaseElement


class QATechPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://qatechhub.com'

    def go(self):
        self.driver.get(self.url)

    @property
    def button1(self):
        locator = (By.ID, 'search-button')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )
