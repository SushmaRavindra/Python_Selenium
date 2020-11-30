from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# driver = webdriver.Chrome("./chromedriver")

# driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/iframe.html")

# sleep(5)

# data = ["username, password", [("bill.gates", "password123"), ("steve.jobs", "password123")]]
import xlrd


def read_objects(filename, sheetname):
    wb = xlrd.open_workbook(filename)
    ws = wb.sheet_by_name(sheetname)
    rows = ws.get_rows()
    for index, row in enumerate(rows):
        if row[0].value == "test_shopping":
            headers = ws.row_values(index-1, start_colx=2)
            return headers


def read_data(filename, sheetname):
    data = []
    wb = xlrd.open_workbook(filename)
    ws = wb.sheet_by_name(sheetname)
    rows = ws.get_rows()
    for index, row in enumerate(rows):
        if row[0].value == "test_login":
            temp = ws.row_values(index, start_colx=1)
            temp = tuple([item for item in temp if item])
            if temp[0] == "Yes":
                data.append(temp)
    return data


print(read_data("TestData.xlsx", "Shopping"))
# headers = next(rows)    # Skipping the Headers


# # Dictionary Comprehension
# data = {row[0].value: (row[1].value, row[2].value) for row in rows}
#
# print(data["txt_email"])
# print(data["txt_password"])




# frame = driver.find_element_by_xpath("//iframe[@name='frame1']")
# driver.switch_to.frame(frame)
#
# sleep(2)
#
# driver.find_element_by_xpath("//a[text()='Business']").click()

# books = ["Fiction", 'Health Book', "Science"]
#
# for book in books:
#     _xpath = f"//a[text()='{book}']/../..//input[@value='Add to cart']"
#     driver.find_element_by_xpath(_xpath).click()
#     sleep(1)
#
# sleep(5)
#
# driver.find_element_by_xpath("//span[text()='Shopping cart']").click()
#
# sleep(3)
#
# _xpath = "(//a[text()='Health Book'])[2]/../..//input[@type='checkbox']"
#
# driver.find_element_by_xpath(_xpath).click()

# quantities = {"Science": 2, "Health Book": 3, "Fiction": 4}
# for book, quantity in quantities.items():
#     _xpath = f"(//a[text()='{book}'])[2]/../..//input[@type='text']"
#     driver.find_element_by_xpath(_xpath).clear()
#     driver.find_element_by_xpath(_xpath).send_keys(quantity)
#     sleep(1)


# price_tag = {
#     "$25 Virtual Gift Card": 25.00,
#     "14.1-inch Laptop": 1590.00,
#     "Simple Computer": 800.00
# }
# for item, price in price_tag.items():
#     _xpath = f"//a[text()='{item}']/../..//span[@class='price actual-price']"
#     actual_price = driver.find_element_by_xpath(_xpath).text
#     if price == float(actual_price):
#         print("PASS")
#     else:
#         print('FAIL')



# ratings = ['Excellent', 'Very bad', 'Good', 'Poor']
# for rating in ratings:
#     _xpath = f"//label[text()='{rating}']/..//input[@type='radio']"
#     driver.find_element_by_xpath(_xpath).click()
#     sleep(1)

# driver.find_element_by_xpath("//a[text()='Python 3.8.6']/../..//a[text()='Release Notes']").click()



# driver.find_element_by_xpath("//td[text()='Java']/..//input[@name='download']").click()



# driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys("Nike")
# sleep(3)
#
# driver.find_element_by_xpath("//li[text()='Nike Shoes']").click()

# driver.find_element_by_xpath("//input[@name='keyword']").send_keys("Python")
#
# sleep(3)
#
# driver.find_element_by_xpath("//strong[text()=' fresher']").click()



# driver.find_element_by_xpath("//input[@id='inline-search-input-query']").send_keys("Python")
#
# driver.find_element_by_xpath("//input[@name='location']").send_keys("Bangalore")
#
# sleep(3)
#
# driver.find_element_by_xpath("//li[contains(text(), 'Bangalore, India')]").click()
#
# sleep(2)
#
# driver.find_element_by_xpath("//button[contains(text(), 'Search')]").click()
#
# sleep(5)
#
# titles = driver.find_elements_by_xpath("//h2[@itemprop='title']")
#
#
# for _title in titles:
#     print(_title.text.strip())
#
#
# _xpath_qualification = "//div[@itemprop='qualifications']/ul"
#
# quls = driver.find_elements_by_xpath(_xpath_qualification)
#
# for q in quls:
#     print(q.text.strip())


# driver.find_element_by_xpath("//button[text()='Try it']").click()
#
# sleep(1)
#
# driver.switch_to.alert.accept()
#
# driver.find_element_by_xpath("//button[text()='Try it']").click()
#
# sleep(1)
#
# print(driver.switch_to.alert.text)
#
# sleep(1)
#
# driver.switch_to.alert.dismiss()

# handles = driver.window_handles
#
# for handle in handles[1:]:
#     driver.switch_to.window(handle)
#     driver.close()
#     sleep(1)
# #
# driver.switch_to.window(handles[0])
# #
# sleep(2)
#
# job = "Only Immediate Joiners - Python Developer - Chennai"
# #
# driver.find_element_by_xpath("//input[@name='keyword']").send_keys(job)
# #
# driver.find_element_by_xpath("//button[text()='Search']").click()
# #
# sleep(5)
# #
# titles = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
# #
# titles[0].click()   # Click on Fist Job Title
# #
# sleep(4)
# #
# handles = driver.window_handles
# #
# driver.switch_to.window(handles[1])
# #
# sleep(2)
#
# roles = driver.find_elements_by_xpath("//h2[text()='Job description']/..//ul[1]/li")
#
# for role in roles:
#     print(role.text)
#     sleep(1)

#
# driver.find_element_by_xpath("//button[text()='Register to apply']").click()
#
# sleep(4)
#
# driver.switch_to.window(handles[0])
#
# sleep(3)
#
# driver.close()



# driver.find_element_by_link_text("Twitter").click()
#
# sleep(3)
#
# handles = driver.window_handles
#
# driver.switch_to.window(handles[1])
#
# sleep(2)
#
# driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("Hello")
#
# driver.switch_to.window(handles[0])
#
# sleep(3)
#
# driver.find_element_by_link_text("Register")
#
# driver.switch_to.window(handles[1])
#
# sleep(3)
#
# driver.close()
#
# sleep(3)
#
# driver.switch_to.window(handles[0])
#
# sleep(3)
#
# driver.close()

# for handle in handles:
#     driver.switch_to.window(handle)
#     if driver.title == "HSBC":
#         driver.close()
#     sleep(1)





# driver.find_element_by_xpath("//button[text()='Click Me']").click()

# w = WebDriverWait(driver, 10)
# w.until(ec.invisibility_of_element_located(("xpath", "//div[@id='loader']")))

# driver.find_element_by_name("fname").send_keys("Hello")

# actions = ActionChains(driver)
# button = driver.find_element_by_xpath("//button[text()='Double-click me']")
# actions.double_click(button).perform()

# actions.send_keys(Keys.PAGE_DOWN).perform()
# sleep(1)
# actions.send_keys(Keys.PAGE_UP).perform()
# sleep(1)
# actions.send_keys(Keys.ARROW_DOWN).perform()
# sleep(1)
# actions.send_keys(Keys.ARROW_DOWN).perform()
# sleep(1)
# actions.send_keys(Keys.ARROW_DOWN).perform()
# sleep(1)
# actions.send_keys(Keys.ARROW_UP).perform()
# sleep(1)
# actions.send_keys(Keys.ARROW_UP).perform()
# sleep(1)
# actions.send_keys(Keys.ARROW_UP).perform()
# sleep(1)
# actions.send_keys(Keys.TAB).perform()
# sleep(1)
# actions.send_keys(Keys.TAB).perform()
# sleep(1)
# actions.send_keys(Keys.ENTER).perform()


# kids = driver.find_element_by_xpath("(//a[text()='Kids'])[1]")
#
# actions.move_to_element(kids).perform()

# jobs = driver.find_element_by_xpath("//div[text()='Jobs']")
# actions.move_to_element(jobs).perform()
#
# sleep(1)
#
# rec = driver.find_element_by_xpath("//div[text()='Recruiters']")
# actions.move_to_element(rec).perform()
#
# sleep(1)
#
# companies = driver.find_element_by_xpath("//div[text()='Companies']")
# actions.move_to_element(companies).perform()
#
# sleep(1)
#
# tools = driver.find_element_by_xpath("//div[text()='Tools']")
# actions.move_to_element(tools).perform()







# careers = driver.find_element_by_xpath("//a[text()='Careers']")
#
# actions.move_to_element(careers).perform()


# def click_element(locator):
#     loctype, locvalue = locator
#     driver.find_element(loctype, locvalue).click()
#
#
# def enter_text(locator, *, value):
#     loctype, locvalue = locator
#     driver.find_element(loctype, locvalue).clear()
#     driver.find_element(loctype, locvalue).send_keys(value)
#
#
# def select_item(locator, *, item):
#     loctype, locvalue = locator
#     ele = driver.find_element(loctype, locvalue)
#     s = Select(ele)
#     if isinstance(item, str):
#         s.select_by_visible_text(item)
#     else:
#         s.select_by_index(item)
#
#
# def select_items(locator, *, items):
#     for item in items:
#         select_item(locator, item=item)
#
#
# def get_current_item(locator):
#     loctype, locvalue = locator
#     ele = driver.find_element(loctype, locvalue)
#     s = Select(ele)
#     return s.first_selected_option.text.strip()


# select_item(("id", "standard_cars"), item="Honda")
# print(get_current_item(("id", "standard_cars")))
# sleep(1)
# select_item(("id", "standard_cars"), item="Audi")
# print(get_current_item(("id", "standard_cars")))
# sleep(1)
# select_item(("id", "standard_cars"), item="Mercedes")
# print(get_current_item(("id", "standard_cars")))
# sleep(1)
# select_item(("id", "standard_cars"), item="Jaguar")
# sleep(1)
# select_items(("id", "multiple_cars"), items=['Honda', 'Audi', 'Jaguar'])

# click_element((By.LINK_TEXT, "Register"))
# sleep(1)
# click_element((By.ID, "gender-male"))
# sleep(1)
# enter_text((By.NAME, "FirstName"), value="Hello")
# sleep(1)
# enter_text((By.NAME, "LastName"), value="World")
# sleep(1)
# enter_text((By.ID, "Email"), value="Hello.World@company.com")
# sleep(1)
# enter_text((By.NAME, "Password"), value="Password123")
# sleep(1)
# enter_text((By.NAME, "ConfirmPassword"), value="Password123")
# sleep(1)
# click_element((By.NAME, "register-button"))


# ele = driver.find_element_by_id("multiple_cars")
#
# s = Select(ele)
#
# s.select_by_visible_text("Audi")
# s.select_by_visible_text("Honda")
# s.select_by_visible_text("Mercedes")
#
# opts = s.options
#
# items = []
# for opt in opts:
#     items.append(opt.text)
#
# for item in items:
#     s.select_by_visible_text(item)
#     sleep(0.1)
#
# sleep(3)
#
# s.deselect_by_visible_text("Audi")
# sleep(1)
# s.deselect_by_visible_text("Mini")
#
# s.deselect_by_value("7")
#
# s.deselect_by_index(10)

# s.deselect_all()

#
# for index, item in enumerate(items):
#     print(index, '--->', item)
#     sleep(1)


# s.select_by_visible_text("Honda")
#
# print(s.first_selected_option.text)

# for item in reversed(items):
#     s.select_by_visible_text(item)
#     sleep(0.5)

# s.select_by_visible_text("Audi")
# sleep(1)
# s.select_by_visible_text("Mercedes")
# sleep(1)
# s.select_by_visible_text("Honda")
# sleep(1)
# s.select_by_index(10)
# sleep(1)
# s.select_by_index(4)
# sleep(1)
# s.select_by_value("5")
# sleep(1)
# s.select_by_value("7")











# lst = driver.find_element_by_id("standard_cars")
# s = Select(lst)
#
# opts = s.options
#
# items = [opt.text for opt in opts]

# for item in items:
#     print(item)


# for index, item in enumerate(items):
#     if item == 'Mercedes':
#         s.select_by_visible_text(item)
#         print(f'{item} present at index {index}')

# print(len(items))

# if "Honda" in items:
#     s.select_by_visible_text("Honda")
# else:
#     print('Honda not present in the lisbox')



# s.select_by_visible_text("Honda")
# sleep(1)
# s.select_by_visible_text("Mercedes")
# sleep(1)
# s.select_by_visible_text("Toyota")
# sleep(1)
# s.select_by_index(3)
# sleep(1)
# s.select_by_index(4)
# sleep(1)
# s.select_by_value("4")
# sleep(1)
# s.select_by_value("9")

# driver.find_element_by_name("keyword").send_keys("Python")
# sleep(1)
# driver.find_element_by_xpath("//button[text()='Search']").click()
# sleep(5)
#
# titles = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
#
# for _title in titles:
#     print(_title.text)
#     sleep(1)

# links = driver.find_elements_by_partial_link_text("Python")
#
# for link in links:
#     print(link.text)

# print(driver.find_element_by_link_text("Register").get_attribute("spam"))

# images = driver.find_elements_by_xpath("//img")
#
# for image in images:
#     print(image.get_attribute("alt"))

# for link in links:
#     if "Python" in link.text:
#         print(link.text, ":", link.get_attribute("href"))

# for element in elements[::-1]:
#     element.click()
#     sleep(1)

# for i in range(len(elements)-1, -1, -1):
#     elements[i].click()
#     sleep(1)

# for item in elements[::2]:
#     item.click()
#     sleep(1)

# elements[0].click()
# sleep(1)
# elements[-1].click()

# driver.find_element_by_xpath("//input[@id='pollanswers-2']").click()
#
# sleep(1)
#
# driver.find_element_by_xpath("//input[@value='Vote']").click()


# driver.find_element_by_xpath("(//input[@value='Add to cart'])[6]").click()
#
# sleep(2)
#
# driver.find_element_by_xpath("//input[@name='product_attribute_75_5_31']").click()
#
# sleep(1)
#
# driver.find_element_by_xpath("(//input[@value='Add to cart'])[1]").click()
#
# sleep(5)
#
# driver.find_element_by_xpath("//span[text()='Shopping cart']").click()
#
# sleep(1)
#
# driver.find_element_by_xpath("//input[@name='termsofservice']").click()
#
# sleep(1)
#
# driver.find_element_by_xpath("//button[contains(text(), 'Checkout')]").click()

# driver.find_element_by_xpath("//input[@name='NewsletterEmail']").send_keys("a.a@a.com")
#
# sleep(1)
#
# driver.find_element_by_xpath("//input[@value='Subscribe']").click()
#
# sleep(2)
#
# print(driver.find_element_by_xpath("//div[text()='Thank you for signing up! A verification email has been sent. We appreciate your interest.']").is_displayed())

# driver.find_element_by_xpath("//input[@name='keyword']").send_keys("Python")
#
# sleep(3)
#
# driver.find_element_by_xpath("//button[text()='Search']").click()

# driver.find_element_by_xpath("//a[text()='Contact us']").click()
#
# sleep(2)
#
# driver.find_element_by_xpath("//input[@class='fullname']").send_keys("Hello world")
#
# sleep(2)
#
# driver.find_element_by_xpath("//input[@id='Email']").send_keys("a.a@company.com")
#
# sleep(2)
#
# driver.find_element_by_xpath("//textarea[@name='Enquiry']").send_keys("Testing")
#
# sleep(2)
#
# driver.find_element_by_xpath("//input[@name='send-email']").click()


# driver.find_element_by_xpath("//a[text()='Log in']").click()
#
# sleep(2)
#
# driver.find_element_by_xpath("//input[@class='email']").send_keys("bill.gates@company.com")
#
# sleep(2)
#
# driver.find_element_by_xpath("//input[@id='Password']").send_keys("Password123")
#
# sleep(2)
#
# driver.find_element_by_xpath("//input[@value='Log in']").click()
#
# sleep(2)
#
# print(driver.find_element_by_xpath("//a[text()='bill.gates@company.com']").is_displayed())


# driver.find_element_by_xpath("//a[@class='ico-register']").click()
# sleep(1)
# driver.find_element_by_xpath("//input[@id='gender-male']").click()
# sleep(1)
# driver.find_element_by_xpath("//input[@id='FirstName']").send_keys("Hello")
# sleep(1)
# driver.find_element_by_xpath("//input[@name='LastName']").send_keys("World")
# sleep(1)
# driver.find_element_by_xpath("//input[@id='Email']").send_keys("a.a@aa.com")
# sleep(1)
# driver.find_element_by_xpath("//input[@id='Password']").send_keys("Password123")
# sleep(1)
# driver.find_element_by_xpath("//input[@name='ConfirmPassword']").send_keys("Password123")
# sleep(1)
# driver.find_element_by_xpath("//input[@name='register-button']").click()

# driver.find_element_by_xpath("//input[@value='Search store']").send_keys("Computer")
# sleep(1)
# driver.find_element_by_xpath("//input[@value='Search']").click()

# driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys("Firstname")
# sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/input[2]").send_keys("Lastname")
# sleep(2)
# driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys("Company")
# sleep(2)
# driver.find_element_by_xpath("/html/body/div[2]/input[2]").send_keys("Location")

# driver.find_element_by_css_selector("a[class='ico-login']").click()
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[class='email']").send_keys("hello")
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[name='Password']").send_keys("World")
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[value='Log in']").click()

# driver.find_element_by_css_selector("a[class='ico-register']").click()
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[id='gender-male']").click()
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[name='FirstName']").send_keys("Hello")
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[name='LastName']").send_keys("World")
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[name='Email']").send_keys("a.a@aa.com")
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[name='Password']").send_keys("Password123")
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[name='ConfirmPassword']").send_keys("Password123")
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[name='register-button']").click()

# driver.find_element_by_css_selector("input[type='text']").send_keys("Hello")
#
# sleep(1)
#
# driver.find_element_by_css_selector("input[type='password']").send_keys("World")


# driver.find_element_by_link_text("Health Book").click()
#
# sleep(3)
#
# driver.find_element_by_id("add-to-cart-button-22").click()
#
# sleep(5)
#
# driver.find_element_by_partial_link_text("Shopping cart").click()
#
# sleep(1)
#
# driver.find_element_by_name("termsofservice").click()
#
# sleep(1)
#
# driver.find_element_by_name("checkout").click()



# driver.find_element_by_link_text("Contact us").click()
#
# sleep(2)
#
# driver.find_element_by_name("FullName").send_keys("Test")
#
# sleep(2)
#
# driver.find_element_by_id("Email").send_keys("a.a@company.com")
#
# sleep(2)
#
# driver.find_element_by_class_name("enquiry").send_keys("Testing")
#
# sleep(2)
#
# driver.find_element_by_name("send-email").click()

# driver.find_element_by_id("pollanswers-1").click()
# sleep(2)
# driver.find_element_by_id("vote-poll-1").click()








# driver.find_element_by_name("q").send_keys("Computer")
# sleep(2)
# driver.find_element_by_class_name("button-1.search-box-button").click()

# driver.find_element_by_link_text("Log in").click()
#
# driver.find_element_by_id("Email").send_keys("bill.gates@company.com")
# sleep(1)
# driver.find_element_by_name("Password").send_keys("Password123")
# sleep(1)
# driver.find_element_by_class_name("button-1.login-button").click()
# sleep(4)
# print(driver.find_element_by_link_text("bill.gates@company.com").is_displayed())

# driver.find_element_by_link_text("Register").click()
#
# sleep(1)
#
# driver.find_element_by_id("gender-male").click()
#
# sleep(1)
#
# driver.find_element_by_id("FirstName").send_keys("Hello")
#
# sleep(1)
#
# driver.find_element_by_name("LastName").send_keys("World")
#
# sleep(1)
#
# driver.find_element_by_id("Email").send_keys("Hello.world@company.com")
#
# sleep(1)
#
# driver.find_element_by_name("Password").send_keys("Password123")
#
# sleep(1)
#
# driver.find_element_by_name("ConfirmPassword").send_keys("Password123")
#
# sleep(1)
#
# driver.find_element_by_name("register-button").click()



# acutal_title = driver.title
#
# if acutal_title == "Google":
#     print("PASS")
# else:
#     print('FAIL')
#
# driver.refresh()
# driver.forward()
# driver.back()
#
# driver.close()