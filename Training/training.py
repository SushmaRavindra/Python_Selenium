from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.qspiders.com/courses")
time.sleep(5)


f = open('batches.txt', 'w')

_courses = ['Advanced Selenium-Software Testing Course',
            ' Python - Selenium',
            'Api Testing']

for _course in _courses:
    _xpath = f"//span[text()='{_course}']/../..//a[text()='Show batches']"

    driver.find_element_by_xpath(_xpath).click()

    time.sleep(3)

    _branches = driver.find_elements_by_xpath("//td[@class='views-field views-field-field-branch']")
    _dates = driver.find_elements_by_xpath("//td[@class='views-field views-field-field--batch-commencing-date']/span")
    _timings = driver.find_elements_by_xpath("//td[@class='views-field views-field-field--batch-commencing-date-1']/span")

    for _branch, _date, _timing in zip(_branches, _dates, _timings):
        print(_branch.text, '\t', _date.text, '\t', _timing.text, file=f)

    sep = "="
    print(sep*50, file=f)

    driver.find_element_by_xpath("//button[text()='Close']").click()

f.close()


click_element(('link text', "Register"))

click_element(("id", "gender-male"))

enter_text(("name", "FirstName"), value="Sandeep")

enter_text(("name", "LastName"), value="Suryaprasad")

click_element(("id", "register-button"))
class element_to_be_visible_enabled:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        locatortype, locatorvalue = self.locator
        element = driver.find_element(locatortype, locatorvalue)
        if element.is_displayed() and element.is_enabled():
            return True
        else:
            return False


def wait(visible=True, enabled=True, max_timeout=10):
    def decorate(func):
        def wrapper(*args, **kwargs):
            locator, = args
            w = WebDriverWait(driver, max_timeout)
            if visible and enabled:
                w.until(element_to_be_visible_enabled(locator))
            elif visible and not enabled:
                w.until(ec.visibility_of_element_located(locator))
            elif not visible:
                w.until(ec.invisibility_of_element_located(locator))
            return func(*args, **kwargs)
        return wrapper
    return decorate


@wait()
def enter_text(locator, *, value):
    loctype, locvalue = locator
    driver.find_element(loctype, locvalue).clear()
    driver.find_element(loctype, locvalue).send_keys(value)


@wait()
def click_element(locator):
    loctype, locvalue = locator
    driver.find_element(loctype, locvalue).click()


@wait()
def select_item(locator, *, item):
    loctype, locvalue = locator
    element = driver.find_element(loctype, locvalue)
    select = Select(element)
    items = [i.text for i in select.options]
    if item not in items:
        raise ValueError(f"{item} is not present in the listbox")
    if isinstance(item, str):
        select.select_by_visible_text(item)
    else:
        select.select_by_index(item)