from selenium import webdriver


class BaseElement(object):
    def __init__(self, driver, locator, by):
        self.driver = driver
        self.locator = locator
        self.by = by

        self.web_element = None
