from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome('./chromedriver')
driver.get('http://demowebshop.tricentis.com')


def enter_text(locator, *, value):
    loctype, locvalue = locator
    driver.find_element(loctype, locvalue).clear()
    driver.find_element(loctype, locvalue).send_keys(value)


def click_element(locator):
    loctype, locvalue = locator
    driver.find_element(loctype, locvalue).click()


def select_item(locator, *, item):
    ...


click_element(("xpath", "//a[text()='Register']"))
sleep(2)

click_element(("id", "gender-male"))
sleep(2)

enter_text(("name", "FirstName"), value="Steve")
sleep(2)

enter_text(("id", "LastName"), value="Jobs")
sleep(2)

enter_text(("id", "Email"), value="steve.jobs@company.com")
sleep(2)

enter_text(("name", "Password"), value="password123")
sleep(2)

enter_text(("name", "ConfirmPassword"), value="password123")
sleep(2)

click_element(("name", "register-button"))






