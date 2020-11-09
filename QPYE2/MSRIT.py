from selenium import webdriver
import xlrd
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Standard_listbox.html")


def enter_text(locator, *, value):
    loctype, locvaue = locator
    driver.find_element(loctype, locvaue).clear()
    driver.find_element(loctype, locvaue).send_keys(value)


def click_element(locator):
    loctype, locvalue = locator
    driver.find_element(loctype, locvalue).click()


def select_item(locator, *, item):
    loctype, locvalue = locator
    ele = driver.find_element(loctype, locvalue)
    s = Select(ele)
    if isinstance(item, str):
        s.select_by_visible_text(item)
    else:
        s.select_by_index(item)


def select_items(locator, *, items):
    for item in items:
        select_item(locator, item=item)


select_item(("id", "standard_cars"), item="Mercedes")
select_item(("id", "standard_cars"), item=5)

select_items(("id", "multiple_cars"), items=['Audi', 'Mercedes', 'Honda'])

# click_element(("link text", "Register"))
#
# sleep(2)
# click_element(("id", "gender-male"))
#
# sleep(2)
# enter_text(("name", "FirstName"), value="Hello")
#
# sleep(2)
# enter_text(("name", "LastName"), value="World")
#
# sleep(2)
# enter_text(("name", "Email"), value="Hello.World@company.com")
#
# sleep(2)
# enter_text(("name", "Password"), value="admin")
#
# sleep(2)
# enter_text(("name", "ConfirmPassword"), value="admin")
#
# sleep(2)
# click_element(("name", "register-button"))



















# def read_data(sheetname, tc):
#     wb = xlrd.open_workbook("TestData.xlsx")
#     ws = wb.sheet_by_name(sheetname)
#     rows = ws.get_rows()
#
#     for index, row in enumerate(rows):
#         if not row[0].value == tc:
#             continue
#         data = ws.row_values(index-1, start_colx=2)
#         headers = ','.join([item for item in data if item])
#         break
#
#     final_data = []
#     rows = ws.get_rows()
#     for index, row in enumerate(rows):
#         if row[0].value == tc:
#             data = ws.row_values(index, start_colx=1)
#             temp = [item for item in data if item]
#             if temp[0] == "Yes":
#                 final_data.append(tuple(temp))
#     return [headers, final_data]
#
# data = read_data("Shopping", "test_shopping")
#
# h, d = data
#
# print(h)
# print(d)

# headers = next(rows)

# for index, row in enumerate(rows):
#     print(index, row[0].value)

# Dictionary Comprehension
# records = {row[0].value: (row[1].value, row[2].value) for row in rows}









# driver.get("https://www.naukri.com/")
#
# sleep(5)
#
#
# win_handles = driver.window_handles
#
# for handle in win_handles:
#     driver.switch_to.window(handle)
#     if driver.title == "Cognizant":
#         driver.close()

# driver.switch_to.window(win_handles[1])
#
# sleep(2)
#
# driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("Hello")
#
# driver.switch_to.window(win_handles[0])
#
# driver.find_element_by_xpath("//a[text()='Register']").click()
#
# driver.switch_to.window(win_handles[1])
# driver.close()
#
# driver.switch_to.window(win_handles[0])
# driver.close()



# driver.find_element_by_xpath("//input[@id='SE_home_autocomplete']").send_keys("Python Automation")
#
# sleep(2)
#
# driver.find_element_by_xpath("//strong[text()='Python Automation']").click()
#
# sleep(2)
#
# driver.find_element_by_xpath("//input[@value='Search']").click()

# a = ActionChains(driver)

# a.double_click(driver.find_element_by_xpath("//button[text()='Double-click me']")).perform()


# a.send_keys(Keys.TAB)
# a.send_keys(Keys.TAB)
# a.send_keys(Keys.ENTER)
# a.perform()

# a.send_keys(Keys.PAGE_DOWN).perform()
#
# sleep(2)
#
# a.send_keys(Keys.PAGE_UP).perform()
#
# sleep(2)

# a.send_keys(Keys.ARROW_DOWN).perform()
# a.send_keys(Keys.ARROW_DOWN).perform()
# a.send_keys(Keys.ARROW_DOWN).perform()
# a.send_keys(Keys.ARROW_DOWN).perform()
#
# a.send_keys(Keys.ARROW_UP).perform()
# a.send_keys(Keys.ARROW_UP).perform()
# a.send_keys(Keys.ARROW_UP).perform()
# a.send_keys(Keys.ARROW_UP).perform()


# jobs = driver.find_element_by_xpath("//a[text()='Job search']")
#
# a.move_to_element(jobs).perform()
#
# skills = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
#
# a.move_to_element(skills).perform()
#
# driver.find_element_by_xpath("//a[contains(text(), 'Python Jobs')]").click()



# books = ['Health Book', 'Science', 'Fiction']

# items = ['$25 Virtual Gift Card', '14.1-inch Laptop', 'Build your own cheap computer',
#          'Build your own computer', 'Build your own expensive computer', 'Simple Computer']
#
# prices = [25.00, 1590.00, 800.00, 1200.00, 1800.00, 800.00]
#
# d = {'$25 Virtual Gift Card': 25.00,
#      "14.1-inch Laptop": 1590.00,
#      "Build your own cheap computer": 800.00,
#      "Build your own computer": 1200.00,
#      "Build your own expensive computer": 1800.00,
#      "Simple Computer": 800.00
#      }
#
# for item, price in d.items():
#     _xpath = f"//a[text()='{item}']/../..//span[@class='price actual-price']"
#     actual_price = driver.find_element_by_xpath(_xpath).text
#     if price == float(actual_price):
#         print('PASS')
#     else:
#         print('FAIL')


# for book in books:
#     driver.find_element_by_xpath(f"//a[text()='{book}']/../..//input[@value='Add to cart']").click()
#     sleep(2)
#
# sleep(5)
#
# driver.find_element_by_xpath("//span[text()='Shopping cart']").click()

# _xpath = "(//a[text()='Health Book'])[2]/../..//input[@type='text']"
# _xpath = "(//a[text()='Science'])[2]/../..//input[@name='removefromcart']"

# driver.find_element_by_xpath(_xpath).click()

# sleep(2)

# _xpath = "(//a[text()='Health Book'])[2]/../..//input[@name='removefromcart']"
# driver.find_element_by_xpath(_xpath).click()

# sleep(2)

# driver.find_element_by_xpath("//input[@value='Update shopping cart']").click()

# cars = driver.find_element_by_xpath("//select[@id='multiple_cars']")
#
# s = Select(cars)
#
# items = ['Maruti', 'Honda', 'Audi', 'Mercedes', 'Mini']
#
# for item in items:
#     try:
#         s.select_by_visible_text(item)
#         sleep(1)
#     except NoSuchElementException:
#         print(f'{item} was not found in the listbox')
#         continue
#
# opts = s.all_selected_options
#
# for item in opts:
#     print(item.text)
#
# print(s.first_selected_option.text)

# s.deselect_all()

# opts = s.options
# labels = [item.text for item in opts]



# for label in labels:
#     s.select_by_visible_text(label)
#     sleep(0.2)


# opts = s.options

# labels = []
# for opt in opts:
#     labels.append(opt.text)

# labels = [opt.text for opt in opts]
#
# print(s.first_selected_option.text)
#
# s.select_by_visible_text("Honda")
#
# sleep(1)
#
# print(s.first_selected_option.text)
#
# s.select_by_visible_text("Audi")
#
# print(s.first_selected_option.text)

# search_item = 'Mercedes'

# for index, label in enumerate(labels):
#     if search_item == label:
#         s.select_by_visible_text(label)
#         print(f'{search_item} is at index {index}')





# for index, label in enumerate(labels):
#     print(index, "--->", label)




# words = ['hello', 'world']
# elements = driver.find_elements_by_name("spam")

# for element, word in zip(elements, words):
#     element.send_keys(word)
#     sleep(1)




# boxes = driver.find_elements_by_xpath("//input[@name='download']")

# links = driver.find_elements_by_xpath("//a")

# print(driver.find_element_by_name('q').get_attribute("id"))
# print(driver.find_element_by_name('q').get_attribute("class"))
# print(driver.find_element_by_name('q').get_attribute("spam"))

# for link in links:
#     if 'Python' in link.text:
#         print(f"{link.text} {link.get_attribute('href')}")
#         sleep(0.2)

# boxes[0].click()

# boxes[-1].click()

# for box in boxes[::2]:
#     box.click()
#     sleep(1)



# driver.find_element_by_name("spam").send_keys("Hello")

# driver.find_element_by_name("q").send_keys("Computer")
# sleep(1)
# driver.find_element_by_name("q").clear()
# driver.find_element_by_name("q").send_keys(" laptop")


# driver.find_element_by_link_text("Register").click()
#
# sleep(3)
#
# driver.find_element_by_id("gender-male").click()
#
# sleep(1)
#
# driver.find_element_by_name("FirstName").send_keys("Hello")
#
# sleep(1)
#
# driver.find_element_by_name("LastName").send_keys("world")
#
# sleep(1)
#
# driver.find_element_by_id("Email").send_keys("a@a.com")
#
# sleep(1)
#
# driver.find_element_by_name("Password").send_keys("hello")
#
# sleep(1)
#
# driver.find_element_by_id("ConfirmPassword").send_keys("hello")
#
# sleep(1)
#
# driver.find_element_by_xpath("//input[@value='Register']").click()



# email = driver.find_element_by_name("NewsletterEmail")

# email = driver.find_element_by_id("newsletter-email")

# email.send_keys("Hello world")

# driver.find_element_by_partial_link_text("Log").click()
# General Syntax of css selector expression

# HTML[property="value"]

# driver.find_element_by_css_selector("input[type='text']").send_keys("Hello")
# driver.find_element_by_css_selector("input[type='password']").send_keys("world")

# driver.find_element_by_css_selector("input[value='Search store']").send_keys("Computer")
# driver.find_element_by_css_selector("input[value='Search']").click()

# driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys("Hello")
# driver.find_element_by_xpath("/html/body/div[1]/input[2]").send_keys("world")
# driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys("company")
# driver.find_element_by_xpath("/html/body/div[2]/input[2]").send_keys("location")

# driver.find_element_by_xpath("//input[@value='Search store']").send_keys("Computer")
# driver.find_element_by_xpath("//input[@class='button-1 search-box-button']").click()

# driver.find_element_by_xpath("//a[text()='Register']").click()
