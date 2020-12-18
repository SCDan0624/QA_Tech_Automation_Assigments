class QATechPage:

    def __init__(self, driver):
        self.driver = driver

    def type_into_input(self, text):
        inpt = self.driver.find_element_by_id('search-field')
        print(inpt)
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
