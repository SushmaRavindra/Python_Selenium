from selenium import webdriver

# What is WebDriver?
# WebDriver is an API that interacts with Real Browsers through respective driver exe.
# Selenium Code to Launch Chrome Browser
driver = webdriver.Chrome('/home/sandeep/Desktop/Selenium/chromedriver')


# Selenium Code to Navigate to Google.
# Comment: We should specify the complete URL of the application
# starting protocol. get method makes selenium to wait till the
# web page is completely loaded
driver.get("http://google.com")


# Selenium Code to refresh the browser
driver.refresh()

# Selenium Code to Maximize the browser
driver.maximize_window()

# Selenium Code to click on browser forward button
driver.forward()

# Selenium Code to click on browser back button
driver.back()

# Selenium Code to fetch the title of the web page
driver.title

# Selenium Code to get the current URL
driver.current_url