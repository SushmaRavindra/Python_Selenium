from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome('./chromedriver')
# driver.get("http://www.qspiders.com/")
# time.sleep(5)
#
# menus = ['About', 'Blog', 'Projects', 'Contact']
#
# menus = driver.find_elements_by_xpath("//a")
# ele1 = driver.find_element_by_xpath("//a[text()='Gallery ']")
# ele2 = driver.find_element_by_xpath("//a[text()='Recruitment Drive']")
#
# actions = ActionChains(driver)
# actions.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(1)
# actions.send_keys(Keys.PAGE_DOWN).perform()
# actions.send_keys(Keys.ESCAPE).perform()
# actions.send_keys(Keys.ENTER).perform()
# actions.send_keys(Keys.PAGE_UP).perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ARROW_UP).perform()
#
# for _ in range(0, 5):
#     actions.send_keys("\ue015").perform()
#     time.sleep(1)
#
# for _ in range(0, 5):
#     actions.send_keys("\ue013").perform()
#     time.sleep(1)
#
# actions.move_to_element(ele1).perform()
# time.sleep(1)
# actions.move_to_element(ele2).perform()
# time.sleep(1)
# ele2.click()


# links = driver.find_elements_by_xpath("//ul[@id='header-nav-bar']//a")
# f = open('url.txt', 'w')
# for link in links:
#     text = link.text
#     url = link.get_attribute("href")
#     print(f'{text:<20} {url:<40}', file=f)
# f.close()

# f = open('batches.csv', 'w')
#
# _courses = ['Advanced Selenium-Software Testing Course',
#             ' Python - Selenium',
#             'Api Testing']
#
# print('Course, Branch, Date, Timings', file=f)
#
# for _course in _courses:
#     _xpath = f"//span[text()='{_course}']/../..//a[text()='Show batches']"
#
#     driver.find_element_by_xpath(_xpath).click()
#
#     time.sleep(3)
#
#     _branches = driver.find_elements_by_xpath("//td[@class='views-field views-field-field-branch']")
#     _dates = driver.find_elements_by_xpath("//td[@class='views-field views-field-field--batch-commencing-date']/span")
#     _timings = driver.find_elements_by_xpath("//td[@class='views-field views-field-field--batch-commencing-date-1']/span")
#
#     for _branch, _date, _timing in zip(_branches, _dates, _timings):
#         print(_course, ',', _branch.text, ',', _date.text, ',', _timing.text, file=f)
#
#     # sep = "="
#     # print(sep*50, file=f)
#
#     driver.find_element_by_xpath("//button[text()='Close']").click()
#
# f.close()
#

# click_element(('link text', "Register"))
#
# click_element(("id", "gender-male"))
#
# enter_text(("name", "FirstName"), value="Sandeep")
#
# enter_text(("name", "LastName"), value="Suryaprasad")
#
# click_element(("id", "register-button"))
# class element_to_be_visible_enabled:
#     def __init__(self, locator):
#         self.locator = locator
#
#     def __call__(self, driver):
#         locatortype, locatorvalue = self.locator
#         element = driver.find_element(locatortype, locatorvalue)
#         if element.is_displayed() and element.is_enabled():
#             return True
#         else:
#             return False
#
#
# def wait(visible=True, enabled=True, max_timeout=10):
#     def decorate(func):
#         def wrapper(*args, **kwargs):
#             locator, = args
#             w = WebDriverWait(driver, max_timeout)
#             if visible and enabled:
#                 w.until(element_to_be_visible_enabled(locator))
#             elif visible and not enabled:
#                 w.until(ec.visibility_of_element_located(locator))
#             elif not visible:
#                 w.until(ec.invisibility_of_element_located(locator))
#             return func(*args, **kwargs)
#         return wrapper
#     return decorate
#
#
# @wait()
# def enter_text(locator, *, value):
#     loctype, locvalue = locator
#     driver.find_element(loctype, locvalue).clear()
#     driver.find_element(loctype, locvalue).send_keys(value)
#
#
# @wait()
# def click_element(locator):
#     loctype, locvalue = locator
#     driver.find_element(loctype, locvalue).click()
#
#
# @wait()
# def select_item(locator, *, item):
#     loctype, locvalue = locator
#     element = driver.find_element(loctype, locvalue)
#     select = Select(element)
#     items = [i.text for i in select.options]
#     if item not in items:
#         raise ValueError(f"{item} is not present in the listbox")
#     if isinstance(item, str):
#         select.select_by_visible_text(item)
#     else:
#         select.select_by_index(item)

import csv


def make_tuple(row):
    return tuple(row)


def make_dict(row):
    return {
        "country": row[0],
        "_date": row[1],
        "cases": row[2],
        "per_mil": row[3]
    }


class Covid:
    def __init__(self, country, cases, _date, per_mil):
        self.country = country
        self.cases = cases
        self._date = _date
        self.per_mil = per_mil


# class Covid:
#     __slots__ = ['country', 'cases', '_date', 'per_mil']
#
#     def __init__(self, country, cases, _date, per_mil):
#         self.country = country
#         self.cases = cases
#         self._date = _date
#         self.per_mil = per_mil

# from collections import namedtuple
# Covid = namedtuple('Covid', ['country', 'cases', 'date_', 'per_mil'])

def make_instance(row):
    return Covid(row[0], row[1], row[2], row[3])

def make_list(row):
    return list(row)

import tracemalloc

def memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        print(tracemalloc.get_traced_memory())
        tracemalloc.stop()
        return result
    return wrapper


@memory
def read_csv():
    records = []
    with open('_covid_data.csv', 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)    # headers
        # make Record
        for row in rows:
            records.append(make_list(row))
    return records



# d = read_csv()

# for item in d:
#     print(item)


d1 = {'a': 1, 'b': 2}
d2 = {'a': 3, 'b': 4}
a = dict([(1, 2), (3, 4)])
print(a)

print(id(d1))
print(id(d2))

for key, value in d1.items():
    print(key, '\t', id(key))

for key, value in d2.items():
    print(key, '\t', id(key))



class Spam(object):
    __slots__ = ('a', 'b')
    def __init__(self, a, b):
        self.a = a
        self.b = b


s1 = Spam(1, 2)
s2 = Spam(3, 4)

print(id(s1.__dict__))
print(id(s2.__dict__))

for key, value in s1.__dict__.items():
    print(key, '\t', id(key))

for key, value in s2.__dict__.items():
    print(key, '\t', id(key))

