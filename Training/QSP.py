from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Progressbar.html")


def click_element(locator):
    loctype, locvalue = locator
    # Call a Function that Checks if the element is visible and enabled
    # Goahead and write a decorator (Visibility and enabled)
    driver.find_element(loctype, locvalue).click()


def enter_text(locator, *, value):
    loctype, locvalue = locator
    driver.find_element(loctype, locvalue).send_keys(value)


def select_item(locator, *, item):
    loctype, locvalue = locator
    element = driver.find_element(loctype, locvalue)
    select = Select(element)
    if isinstance(item, str):
        select.select_by_visible_text(item)
    else:
        select.select_by_index(item)
    sleep(1)


def select_items(locator, *, items):
    for item in items:
        select_item(locator, item=item)


def get_all_options(locator):
    loctype, locvalue = locator
    element = driver.find_element(loctype, locvalue)
    select = Select(element)
    opts = select.options
    items = [opt.text for opt in opts]
    return items


w = WebDriverWait(driver, timeout=10)
driver.find_element_by_xpath("//button[text()='Click Me']").click()
# element = driver.find_element_by_xpath("//div[text()='100%']")
e = ec.visibility_of_element_located(("xpath", "//div[text()='100%']"))
w.until(e)
# enter_text(("name", "fname"), value="Hello")

# def select_item(loctype, locvalue, item, by_value=False):
#     element = driver.find_element(loctype, locvalue)
#     select = Select(element)
#     if by_value:
#         select.select_by_value(item)
#     elif isinstance(item, str):
#         select.select_by_visible_text(item)
#     else:
#         select.select_by_index(item)
#     sleep(1)

# element = driver.find_element_by_id("standard_cars")
# select = Select(element)
# opts = select.options

# items = []
# for opt in opts:
#     items.append(opt.text)

# Using List Comprehension
# items = [opt.text for opt in opts]

# for item in items[::-1]:
#     select.select_by_visible_text(item)
#     sleep(1)
# items = get_all_options("id", "standard_cars")
# for item in items:
#     select_item("id", "standard_cars", item)

# Check if Mercedes is there
# _search_car = "Mercedes"
# for index, item in enumerate(items):
#     if item == _search_car:
#         print(f'Item Found : {item} at index {index}')

# Selecting All the items form Multi Select Listbox
# select_items('id', 'multiple_cars', items)


# for i in range(len(items)-1, -1, -1):
#     select.select_by_visible_text(items[i])
#     sleep(1)


# select_item("id", "standard_cars", "Audi")
# select_item("id", "standard_cars", 10)
# select_items("id", "multiple_cars", ['Audi', 'Mercedes', 'Mini', 3, 10])
# click_element("xpath", "//a[text()='Register']")
# enter_text("name", "FirstName", "Hello")
# click_element("id", "gender-male")
# click_element("name", "register-button")

# books = ['Fiction', 'Health Book', 'Science', 'Computing and Internet']

# for book in books:
#     _xpath = f"//a[text()='{book}']/../..//input[@value='Add to cart']"
#     driver.find_element_by_xpath(_xpath).click()
#     sleep(1)

# _books = ['Computing and Internet',
#           "Copy of Computing and Internet EX",
#           "Fiction",
#           "Fiction EX",
#           "Health Book",
#           "Science"
#           ]
#
# _prices = [10.00, 10.00, 24.00, 24.00, 10.00, 51.00]
#
# d = {'Computing and Internet': 10.00, 'Copy of Computing and Internet EX': 10.00,
#
#      "Fiction": 24.00, "Fiction EX": 24.00, "Health Book": 10.00, "Science": 51.00
#     }

# Alternate Method
# dd = dict(zip(_books, _prices))


# for _book, _price in zip(_books, _prices):
#     _xpath = f"//a[text()='{_book}']/../..//span[@class='price actual-price']"
#     actual_price = float(driver.find_element_by_xpath(_xpath).text)
#     if _price == actual_price:
#         print('PASS')
#     else:
#         print('FAIL')

# for _book, _price in d.items():
#     _xpath = f"//a[text()='{_book}']/../..//span[@class='price actual-price']"
#     actual_price = float(driver.find_element_by_xpath(_xpath).text)
#     if _price == actual_price:
#         print('PASS')
#     else:
#         print('FAIL')
