from selenium import webdriver


class QATechPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://qatechhub.com'

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        inpt = self.driver.find_element_by_id('search-field')
        inpt.clear()
        inpt.send_keys(text)
        return None

    def get_input_text(self):
        inpt = self.driver.find_element_by_id('seach-field')
        elem_text = inpt.get_attribute('value')
        return elem_text

    def search_button(self):
        button = self.driver.find_element_by_id('search-button')
        button.click()
        return None

# Test Here


# Open the Firefox browser
driver = webdriver.Chrome()

qa_page = QATechPage(driver)
qa_page.go()
qa_page.type_into_input('it worked!')
print(qa_page.get_input_text())
