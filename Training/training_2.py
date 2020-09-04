from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")
time.sleep(3)


def enter_text(locator, *, value):
    locatortype, locatorvalue = locator
    driver.find_element(locatortype, locatorvalue).clear()
    driver.find_element(locatortype, locatorvalue).send_keys(value)


def click_element(locator):
    locatortype, locatorvalue = locator
    driver.find_element(locatortype, locatorvalue).click()


click_element(("xpath", "//a[text()='Register']"))
# driver.find_element_by_xpath("//a[text()='Register']").click()
time.sleep(1)
click_element(("id", "gender-male"))
# driver.find_element_by_id("gender-male").click()
time.sleep(1)
enter_text(("name", "FirstName"), value="Sandeep")
# driver.find_element_by_name("FirstName").send_keys("Hello")
time.sleep(1)
enter_text(("name", "LastName"), value="Suryaprasad")
# driver.find_element_by_name("LastName").send_keys("World")
time.sleep(1)
click_element(("name", "register-button"))
# driver.find_element_by_name("register-button").click()




