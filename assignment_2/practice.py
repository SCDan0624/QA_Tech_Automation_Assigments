from selenium import webdriver

# Open the Firefox browser
driver = webdriver.Chrome()

# Navigate to “http://qatechhub.com
driver.get('http://www.fb.com')

# Check current URL
url = driver.current_url
print(url)

assert url == 'https://www.facebook.com/'
print("URL confirmed")
