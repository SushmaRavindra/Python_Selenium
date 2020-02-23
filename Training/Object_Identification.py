from selenium import webdriver

# Selenium Code to Identify webelement using name property
driver = webdriver.Chrome('/home/sandeep/Desktop/Selenium/chromedriver')
driver.get("http://google.com")

# Enters 'Python' in google search text box
driver.find_element_by_name("q").send_keys("Python")

# Selenium Code to Identify webelement using ID property
driver.get("http://demowebshop.tricentis.com/")
driver.find_element_by_id("small-searchterms").send_keys("Computer")

# Selenium Code to Identify webelement using Link Text
driver.find_element_by_link_text("Register").click()

# Selenium Code to Identify webelement using Partial Link Text
driver.find_element_by_partial_link_text("Shopping").click()