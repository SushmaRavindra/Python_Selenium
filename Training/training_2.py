from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Tables.html")

time.sleep(3)

driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
# General Form of CSS Selector
# HTMLTAG[Property=value]

# driver.find_element_by_css_selector("input[type='text']").send_keys("Sandeep")
# driver.find_element_by_css_selector("input[type='password']").send_keys("Password123")


# driver.find_element_by_link_text("Register").click()
#
# time.sleep(1)
#
# driver.find_element_by_id("gender-male").click()
#
# time.sleep(1)
#
# driver.find_element_by_name("FirstName").send_keys("Sandeep")
#
# time.sleep(1)
#
# driver.find_element_by_id("LastName").send_keys("Suryaprasad")
#
# time.sleep(1)
#
# driver.find_element_by_name("register-button").click()
