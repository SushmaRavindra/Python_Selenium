from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome('./chromedriver')
driver.get('file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Loading.html')

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
        s.select_by_visible_text(item)
    elif isinstance(item, int):
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

sleep(1)

driver.find_element_by_xpath("//button[text()='Click Me']").click()

w = WebDriverWait(driver, 15)

loading_icon = driver.find_element_by_id("loader")



## Makes sure that the element is loaded in DOM and visible on the webpage (Double Check)
##v = ec.invisibility_of_element(loading_icon)
v= ec.invisibility_of_element_located(("id", "loader"))
w.until(v)

driver.find_element_by_name("fname").send_keys("Hello")

print('Done!!!')






























##rows = driver.find_elements_by_xpath("//table[@name='os']//tr")
##
##for index, row in enumerate(rows[1:], start=2):
##    tds = driver.find_elements_by_xpath(f"//table[@name='os']/tbody/tr[{index}]/td")
##    for td in tds:
##        print(f'{td.text:>10}', end='')
##    print()


##sleep(1)

##driver.find_element_by_xpath("//button[text()='Click Me']").click()

##w = WebDriverWait(driver, 15)

##loading_icon = driver.find_element_by_id("loader")



# Makes sure that the element is loaded in DOM and visible on the webpage (Double Check)
##v = ec.invisibility_of_element(loading_icon)
##v= ec.invisibility_of_element_located(("id", "loader"))
##w.until(v)

##driver.find_element_by_name("fname").send_keys("Hello")

##print('Done!!!')




















##def enter_text(locator, *, value):
##    loctype, locvalue = locator
##    driver.find_element(loctype, locvalue).clear()
##    driver.find_element(loctype, locvalue).send_keys(value)
##
##
##def click_element(locator):
##    loctype, locvalue = locator
##    driver.find_element(loctype, locvalue).click()
##
##
##def select_item(locator, *, item):
##    loctype, locvalue = locator
##    lst_box = driver.find_element(loctype, locvalue)
##    s = Select(lst_box)
##    opts = s.options
##    items = [opt.text for opt in opts]
##    if isinstance(item ,str):
##        s.select_by_visible_text(item)
##    elif isinstance(item, int):
##        s.select_by_index(item)
##    else:
##        raise TypeError
##
##def select_multiple_items(locator, *, items):
##    for item in items:
##        try:
##            select_item(locator, item=item)            
##        except NoSuchElementException:
##            print(f'{item} not found in the listbox')
##            continue
    


##select_multiple_items(("id", "multiple_cars"), items=["Audi", "Maruti", "Honda", "Ford", 3, 5])
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






