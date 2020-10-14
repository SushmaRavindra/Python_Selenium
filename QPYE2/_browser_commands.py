from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome('./chromedriver')
driver.get('file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Standard_listbox.html')
sleep(2)

def enter_text(locator, *, value):
    loctype, locvalue = locator
    driver.find_element(loctype, locvalue).clear()
    driver.find_element(loctype, locvalue).send_keys(value)


def click_element(locator):
    loctype, locvalue = locator
    driver.find_element(loctype, locvalue).click()


def select_item(locator, *, item):
    loctype, locvalue = locator
    lst_box = driver.find_element(loctype, locvalue)
    s = Select(lst_box)
    opts = s.options
    items = [opt.text for opt in opts]
    if isinstance(item ,str):
##        if not item in items:
##            raise ValueError(f'{item} not found in the listbox')
        s.select_by_visible_text(item)
    elif isinstance(item, int):
##        if item > len(items)-1:
##            raise ValueError(f'Item with {item} does not exist')
        s.select_by_index(item)
    else:
        raise TypeError

def select_multiple_items(locator, *, items):
    for item in items:
        try:
            select_item(locator, item=item)            
        except NoSuchElementException:
            print(f'{item} not found in the listbox')
            continue
    


select_multiple_items(("id", "multiple_cars"), items=["Audi", "Maruti", "Honda", "Ford", 3, 5])
##sleep(2)
##
##select_item(("id", "standard_cars"), item=8)
##sleep(2)
##
##select_item(("id", "standard_cars"), item="Jaguar")
##sleep(2)
##
##select_item(("id", "standard_cars"), item=14)
##sleep(2)

##select_item(("id", "standard_cars"), item="Maruti")




##click_element(("xpath", "//a[text()='Register']"))
##sleep(2)
##
##click_element(("id", "gender-male"))
##sleep(2)
##
##enter_text(("name", "FirstName"), value="Steve")
##sleep(2)
##
##enter_text(("id", "LastName"), value="Jobs")
##sleep(2)
##
##enter_text(("id", "Email"), value="steve.jobs@company.com")
##sleep(2)
##
##enter_text(("name", "Password"), value="password123")
##sleep(2)
##
##enter_text(("name", "ConfirmPassword"), value="password123")
##sleep(2)
##
##click_element(("name", "register-button"))






