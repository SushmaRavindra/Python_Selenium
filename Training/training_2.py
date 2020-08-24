from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com/")

time.sleep(3)

driver.find_element_by_link_text("Register").click()

time.sleep(1)

driver.find_element_by_id("gender-male").click()

time.sleep(1)

driver.find_element_by_name("FirstName").send_keys("Sandeep")

time.sleep(1)

driver.find_element_by_id("LastName").send_keys("Suryaprasad")

time.sleep(1)

driver.find_element_by_name("register-button").click()











