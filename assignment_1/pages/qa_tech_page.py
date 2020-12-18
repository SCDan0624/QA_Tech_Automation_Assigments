class QATechPage:

    def __init__(self, driver):
        self.driver = driver

    def type_into_input(self, text):
        input = self.driver.find_element_by_id('search-field')
        print(input)
        input.send_keys(text)
        return None
