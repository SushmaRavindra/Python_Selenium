from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome('./chromedriver')


driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Standard_listbox.html")
time.sleep(3)


def enter_text(locator, *, value):
    locatortype, locatorvalue = locator
    driver.find_element(locatortype, locatorvalue).clear()
    driver.find_element(locatortype, locatorvalue).send_keys(value)


def click_element(locator):
    locatortype, locatorvalue = locator
    driver.find_element(locatortype, locatorvalue).click()


def select_item(locator, *, item):
    locatortype, locatorvalue = locator
    lst_box = driver.find_element(locatortype, locatorvalue)
    s = Select(lst_box)
    items = [opt.text for opt in s.options]
    if isinstance(item, str):
        if item not in items:
            raise ValueError(f'{item} not found in the list')
        s.select_by_visible_text(item)
    else:
        if item > len(items):
            raise IndexError('Index Error')
        s.select_by_index(item)


def select_items(locator, *, items):
    for item in items:
        try:
            select_item(locator, item=item)
            time.sleep(1)
        except (ValueError, IndexError):
            print(f'{item} was not found in the multi select listbox')
            continue



select_items(("id", "multiple_cars"), items=['Maruti', 15, 'Audi', 'Jaguar', 'Mercedes'])

# lst_box = driver.find_element_by_id("standard_cars")

# s = Select(lst_box)
# opts = s.options

# items = []
#
# for item in opts:
#     items.append(item.text)

# items = [item.text for item in opts]

# select_item(('id', 'standard_cars'), item="Maruti")
# time.sleep(1)
# select_item(('id', 'standard_cars'), item=5)
# time.sleep(1)
# select_item(('id', 'standard_cars'), item="Audi")


# click_element(("xpath", "//a[text()='Register']"))
# # driver.find_element_by_xpath("//a[text()='Register']").click()
# time.sleep(1)
# click_element(("id", "gender-male"))
# # driver.find_element_by_id("gender-male").click()
# time.sleep(1)
# enter_text(("name", "FirstName"), value="Sandeep")
# # driver.find_element_by_name("FirstName").send_keys("Hello")
# time.sleep(1)
# enter_text(("name", "LastName"), value="Suryaprasad")
# # driver.find_element_by_name("LastName").send_keys("World")
# time.sleep(1)
# click_element(("name", "register-button"))
# # driver.find_element_by_name("register-button").click()







# lst_box = driver.find_element_by_id("standard_cars")
#
# s = Select(lst_box)
#
#
# opts = s.options
#
# items = [item.text for item in opts]
#
# for item in reversed(items):
#     s.select_by_visible_text(item)

# ele = driver.find_elements_by_name("spam")
#
# txt = ['Hello', 'world']
#
#
# for t, e in zip(txt, ele):
#     e.send_keys(t)