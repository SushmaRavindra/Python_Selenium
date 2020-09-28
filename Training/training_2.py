from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions
import time


driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/")

opts = webdriver.ChromeOptions()
opts.add_argument()


class element_visibility_and_enabled:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        loctype, locvalue = self.locator
        element = driver.find_element(loctype, locvalue)
        if element.is_enabled() and element.is_displayed():
            return True
        else:
            return False


def element_to_be_visible_enabled(locator):
    def wrapper(driver):
        loctype, locvalue = locator
        element = driver.find_element(loctype, locvalue)
        if element.is_displayed() and element.is_enabled():
            return True
        else:
            return False
    return wrapper

MAX_TIMEOUT = 60

def _wait(*, visible=True, enabled=True, is_alert=False):
    def decorate(func):
        w = WebDriverWait(driver, MAX_TIMEOUT)
        def wrapper(*args, **kwargs):
            locator, = args
            if visible and enabled and not is_alert:
                w.until(element_visibility_and_enabled(locator))
            elif visible and not enabled and not is_alert:
                w.until(ec.visibility_of_element_located(locator))
            elif not visible and not is_alert:
                w.until(ec.invisibility_of_element_located(locator))
            elif is_alert:
                w.until(ec.alert_is_present)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@_wait()
def enter_text(locator, *, value):
    locatortype, locatorvalue = locator
    driver.find_element(locatortype, locatorvalue).clear()
    driver.find_element(locatortype, locatorvalue).send_keys(value)


@_wait()
def click_element(locator):
    locatortype, locatorvalue = locator
    driver.find_element(locatortype, locatorvalue).click()


@_wait()
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


@_wait()
def select_items(locator, *, items):
    for item in items:
        try:
            select_item(locator, item=item)
            time.sleep(1)
        except (ValueError, IndexError):
            print(f'{item} was not found in the multi select listbox')
            continue


click_element(("xpath", "//a[text()='Register']"))
click_element(('id', 'gender-male'))
enter_text(("name", "FirstName"), value="Sandeep")
enter_text(("name", "LastName"), value="Suryaprasad")
click_element(("id", "register-button"))




# def element_visibility_enable(locator):
#     def wrapper(*args, **kwargs):
#         loctype, locvalue = locator
#         element = driver.find_element(loctype, locvalue)
#         s = Select(element)
#         items = [opt.text for opt in s.options]
#         if item not in items:
#             return False
#         else:
#             return True
#     return wrapper


# w = WebDriverWait(driver, 15)
# s = element_visibility_and_enabled(("name", "fname"))
# s = element_to_be_visible_enabled(("name", "fname"))
# w.until(s)
# driver.find_element_by_name("fname").send_keys("Hello")











# click_element(("xpath", "//a[text()='Register']"))
# time.sleep(1)
# click_element(("id", "gender-male"))
# time.sleep(1)
# enter_text(("name", "FirstName"), value="Sandeep")
# time.sleep(1)
# enter_text(("name", "LastName"), value="Suryaprasad")
# time.sleep(1)
# click_element(("name", "register-button"))


# select_items(("id", "multiple_cars"), items=['Maruti', 15, 'Audi', 'Jaguar', 'Mercedes'])

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