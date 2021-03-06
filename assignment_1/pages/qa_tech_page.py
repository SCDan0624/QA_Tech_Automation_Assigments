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
        inpt = self.driver.find_element_by_id('search-field')
        elem_text = inpt.get_attribute('value')
        return elem_text

    def search_button(self):
        button = self.driver.find_element_by_id('search-button')
        button.click()
        return None

# Test Setup


driver = webdriver.Chrome()  # Open the Firefox browser
test_value = 'it worked'

# Test
qa_page = QATechPage(driver)
qa_page.go()
qa_page.type_into_input(test_value)
# qa_page.search_button()
txt_from_input = qa_page.get_input_text()
assert txt_from_input == test_value, "Test Failed"
print("Test passed")
