from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Open the Firefox browser
driver = webdriver.Chrome()

# Navigate to “http://qatechhub.com
driver.get('http://www.fb.com')

# Check current URL
url = driver.current_url
print(url)
assert url == 'https://www.facebook.com/'
print("URL confirmed")

# Verify that there is a “Create an account” section on the page.
create_account_css_locator = "a[id='u_0_2']"

# create_account_css_locator = "a#u_0_2" Also works here
create_account_element = driver.find_element_by_css_selector(
    create_account_css_locator)
assert create_account_element.text == 'Create New Account'
print("Create an account section confirmed")
create_account_element.click()


# Fill in the text boxes: First Name, Last Name, Mobile Number or email address,
#  “Re-enter mobile number”, new password.
first_name_xpath = "//input[starts-with(@id, 'u_') and contains(@id, '_b')]"
first_name_element = driver.find_element_by_xpath(first_name_xpath)
print(first_name_element)
