from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')

driver.get("http://demowebshop.tricentis.com/")

sleep(3)

driver.find_element_by_link_text("Register").click()

driver.find_element_by_id("gender-male").click()

driver.find_element_by_name("FirstName").send_keys('Sandeep')

driver.find_element_by_id('LastName').send_keys('gs')

driver.find_element_by_name("Email").send_keys('a.a@company.com')

driver.find_element_by_name('register-button').click()






