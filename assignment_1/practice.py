
from selenium import webdriver

# Open the Firefox browser
driver = webdriver.Chrome()

# Navigate to “http://qatechhub.com
driver.get('http://qatechhub.com')

# Maximize the browser window
driver.maximize_window()

# Checks title
title = driver.title
print(title)

if title == 'QA Automation Tools Trainings and Tutorials | QA Tech Hub':
    print("PASS")
else:
    print("FAIL")

# Navigate to facebook
driver.get('https://www.facebook.com')
print("Here at Facebook")

# Navigate back to qatech
driver.back()
print('Back at QA Tech')

# Print URL of current page
print(driver.current_url)

# Navigate forward
driver.forward()
print("Moved forward to Facebook")

# Reload page
driver.refresh()
print("Driver refreshed")

# Close driver
print("Closing browser")
driver.close()
