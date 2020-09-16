from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/iframe.html")

driver.switch_to.frame(0)
driver.find_element_by_xpath("//a[text()='Business']").click()
driver.switch_to.default_content()
driver.find_element_by_xpath("//a[text()='Google']").click()

# import csv
# import tracemalloc
# from collections import defaultdict
#
#
# def read_csv():
#     with open('flights.csv') as f:
#         return list(csv.DictReader(f))  # Iterator
#
#
# def read_csv_as_columns():
#     cols = defaultdict(list)
#     with open('flights.csv') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             for header, item in zip(headers, row):
#                 cols[header].append(item)
#     return cols
#
#
# tracemalloc.start()
# d = read_csv_as_columns()
# print(tracemalloc.get_traced_memory())
# tracemalloc.stop()



def greet():
    return 'Hello World'


def demo():
    return 'demo'


def log(func):
    def wrapper(*args, **kwargs):
        print('Wrapping')
        return func(*args, **kwargs)

    return wrapper


def logging(cls):
    for key, value in cls.__dict__.items():
        print(key, '-->', value)
        if callable(value):
            setattr(cls, key, log(value))
    return cls


@logging
class Spam:

    def __init__(self, value, fname, lname):
        self.value = value
        self.fname = fname
        self.lname = lname

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b


@logging
class Demo:
    def __call__(self):
        print('Calling')

# import xlrd
# workbook = xlrd.open_workbook('/Users/sandeep/Documents/Python_Selenium_FW/Data/TestData.xlsx')
# worksheet = workbook.sheet_by_name("Registration")
# rows = worksheet.get_rows()     # Generator Object
#
# # Getting Headers
# for rowno, row in enumerate(rows):
#     if not row[0].value == "test_01":
#         continue
#     headers = worksheet.row_values(rowno-1, start_colx=1)
#     break
# print(tuple(headers))
#
# # Getting Actual Test Data
# rows = worksheet.get_rows()     # Generator Object
# temp_data = []
# for rowno, row in enumerate(rows):
#     if row[0].value == 'test_01':
#         temp = worksheet.row_values(rowno, start_colx=1)
#         temp_data.append(tuple(temp))
#
# final_data = []
# for item in temp_data:
#     if item[0] == 'Yes':
#         final_data.append(item[1:])
#
# print(final_data)
#
#
# headers, data = [("Firstname", "LastNmae"), [("Steve", "JObs"), ("Bill", "Gates")]]
#
#
# print(headers)
# print(data)












# driver = webdriver.Chrome('./chromedriver')
# driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/sample.html")

# elements = driver.find_elements_by_name("spam")
# texts = ['Hello', 'World']

# for element, text in zip(elements, texts):
#     element.send_keys(text)
#     time.sleep(1)

# driver.save_screenshot('demo.png')

# win_handles = driver.window_handles
# for index, win in enumerate(win_handles):
#     if index == 0:
#         continue
#     driver.switch_to.window(win_handles[index])
#     driver.close()
#     time.sleep(1)


# driver.find_element_by_name("myCountry").send_keys("Un")
# time.sleep(1)
# driver.find_element_by_xpath("//strong[text()='United States']").click()

# actions = ActionChains(driver)
# for _ in range(3):
#     actions.send_keys(Keys.ARROW_DOWN).perform()
#     time.sleep(1)
# actions.send_keys(Keys.ENTER).perform()

# driver.find_element_by_xpath("//strong[text()='United States']").click()

# driver.find_element_by_xpath("//div[@class='select-selected']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//div[text()='Honda']").click()

# driver.find_element_by_xpath("//button[text()='Try it']").click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()


#
# for win_id in win_handles:
#     print(win_id)
#
# print(type(win_handles))
#
# for win_handle in win_handles:
#     driver.switch_to.window(win_handle)
#     _title = driver.title
#     if _title == 'Amazon':
#         driver.close()






# driver.find_element_by_xpath("//a[text()='Facebook']").click()
# time.sleep(3)
# win_handles = driver.window_handles
# driver.switch_to.window(win_handles[1])
#
# time.sleep(2)
#
# driver.find_element_by_name("email").send_keys("Hello")
#
# driver.switch_to.window(win_handles[0])
#
# time.sleep(3)
#
# driver.find_element_by_name("q").send_keys("Computer")
#
# time.sleep(2)
#
# driver.find_element_by_xpath("//input[@value='Search']").click()


# actions = ActionChains(driver)
# actions.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(5)
# actions.send_keys(Keys.ENTER).perform()
# driver.find_element_by_xpath("//div[text()='Ford']").click()
# time.sleep(1)
# print(driver.switch_to.alert.text)



# actions = ActionChains(driver)
# element = driver.find_element(By.XPATH, "//button[text()='Double-click me']")
# element = driver.find_element_by_xpath("//button[text()='Double-click me']")
# actions.double_click(element).perform()


# def mouse_hover(locator):
#     locatortype, locatorvalue = locator
#     element = driver.find_element(locatortype, locatorvalue)
#     actions = ActionChains(driver)
#     actions.move_to_element(element).perform()
#
#
# def send_keyboard_input(key):
#     if not key.upper() in {'PAGE_DOWN', 'PAGE_UP', 'ENTER', 'ARROW_DOWN', 'ARROW_UP', 'ESCAPE'}:
#         raise ValueError(f'Invalid Key passed {key}')
#     actions = ActionChains(driver)
#     if key.upper() == 'PAGE_DOWN':
#         actions.send_keys(Keys.PAGE_DOWN).perform()
#     elif key.upper() == 'PAGE_UP':
#         actions.send_keys(Keys.PAGE_UP).perform()
#     elif key.upper() == 'ENTER':
#         actions.send_keys(Keys.ENTER).perform()
#     elif key.upper() == 'ARROW_DOWN':
#         actions.send_keys(Keys.ARROW_DOWN).perform()
#     elif key.upper() == 'ARROW_UP':
#         actions.send_keys(Keys.ARROW_UP).perform()
#     elif key.upper() == 'ESCAPE':
#         actions.send_keys(Keys.ESCAPE).perform()
#
# send_keyboard_input('ENTER')


# menus = ['About', 'Contact']
# for menu in menus:
#     _xpath = f"//a[text()='{menu}']"
#     mouse_hover((By.XPATH, _xpath))
#     time.sleep(1)


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




