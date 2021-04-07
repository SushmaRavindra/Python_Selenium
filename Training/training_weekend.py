from selenium import webdriver



















# Check for visible and enabled!
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         is_visible = super().__call__(driver)    # Calling Parent class __call__ method
#         enabled = driver.find_element(*self.locator).is_enabled()
#         return is_visible and enabled
#
# driver = webdriver.Chrome('./chromedriver')
#
# driver.get("http://demowebshop.tricentis.com/")
#
# driver.find_element("link text", "Register")

# w = WebDriverWait(driver, 10)
# w.until(_visibility_of_element_located(("name", "fname")))
#
# print('Done!')



#
# driver.current_url
#
# # import xlrd
# #
# # # with xlrd.open_workbook('Training/sample.xlsx') as wb:
# # #     ws = wb.sheet_by_name('Covid')
# # #     rows = ws.get_rows()
# # #     for row in rows:
# # #         print(row)
# #
# # wb = xlrd.open_workbook('Training/TestData.xlsx')
# #
# # ws = wb.sheet_by_name("Shopping")
# #
# # rows = ws.get_rows()
# #
# #
# # # print(ws.row_values(1, start_colx=1))
# #
# # # Headers
# # for rowno, row in enumerate(rows):
# #     if row[0].value == "test_shopping":
# #         headers = ws.row_values(rowno-1, start_colx=2)
# #         headers = [ item for item in headers if item]
# #         headers = ','.join(headers)
# #         print(headers)
# #         break
# #
# #
# # rows = ws.get_rows()
# #
# # data = []
# # for rowno, row in enumerate(rows):
# #     if row[0].value == "test_shopping":
# #         # Get the row values of the existing row from column-1
# #         temp_data = ws.row_values(rowno, start_colx=1)
# #         temp_data = [ item  for item in temp_data if item]
# #         print(temp_data)
# #         # Append the list only if the excute column is "Yes"
# #         if temp_data[0] == "Yes":
# #             data.append(tuple(temp_data))
# # print(data)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # login_page = {row[0].value: (row[1].value, row[2].value)  for row in rows }
# #
# #
# #
# #
# # # from selenium import webdriver
# #
# # # driver = webdriver.Chrome('./Training/chromedriver')
# #
# # # driver.get("https://money.rediff.com/index.html")
# #
# # # market = "S&P BSE MidCap"
# #
# # # xpath = f"//div[@class='hmbseindicestable show']//a[text()='{market}']/../..//li"
# #
# # # elements = driver.find_elements_by_xpath(xpath)
# #
# # # for element in elements:
# # #     print(element.text)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # from selenium import webdriver
# # # from time import sleep
# # # from selenium.webdriver.support.select import Select
# # # from selenium.webdriver.common.action_chains import ActionChains
# # # from selenium.webdriver.common.keys import Keys
# # # from selenium.common.exceptions import NoSuchElementException
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.support.wait import WebDriverWait
# # # from selenium.webdriver.support.expected_conditions import visibility_of_element_located, visibility_of, invisibility_of_element_located
# #
# #
# #
# # # driver = webdriver.Chrome("Training/chromedriver")
# # # driver.get("http://demowebshop.tricentis.com/books")
# # # driver.maximize_window()
# #
# # # sleep(3)
# #
# # # ele = driver.find_element_by_xpath("//select[@name='products-orderby']")
# #
# # # print(ele)
# #
# # # s = Select(ele)
# #
# # # s.select_by_visible_text("Name: A to Z")
# #
# # # ele = driver.find_element_by_xpath("//select[@name='products-orderby']")
# #
# # # print(ele)
# #
# # # s = Select(ele)
# #
# # # sleep(4)
# #
# # # s.select_by_visible_text("Created on")
# #
# # # # driver.find_element_by_xpath("//input[@value='Search']").click()
# #
# # # # sleep(1)
# #
# # # # print(driver.switch_to.alert.text)
# #
# # # # driver.switch_to.alert.accept()
# #
# #
# # # # sleep(5)
# #
# # # # handles = driver.window_handles
# #
# # # # Closing all popup's
# # # # for handle in handles[1:]:
# # # #     driver.switch_to.window(handle)
# # # #     driver.close()
# # # #     sleep(1)
# #
# # # # driver.switch_to.window(handles[0])
# #
# # # # sleep(1)
# #
# # # # # Enter Skill
# # # # driver.find_element_by_xpath("//input[@name='keyword']").send_keys("Python")
# #
# # # # driver.find_element_by_xpath("//button[text()='Search']").click()
# #
# # # # sleep(5)
# #
# # # # links = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
# #
# # # # for link in links:
# # # #     print(link.text)
# # # #     sleep(1)
# #
# # # # links[0].click()
# #
# # # # sleep(5)
# #
# # # # handles = driver.window_handles
# #
# # # # driver.switch_to.window(handles[1])
# #
# # # # sleep(2)
# #
# # # # driver.find_element_by_xpath("//button[text()='Login to apply']").click()
# #
# # # # driver.find_element_by_xpath("//a[text()='Twitter']").click()
# # # # sleep(5)
# # # # handles = driver.window_handles
# # # # driver.switch_to.window(handles[1])
# # # # sleep(1)
# # # # driver.find_element_by_xpath("//input[@data-testid='SearchBox_Search_Input']").send_keys("Hello")
# # # # sleep(1)
# # # # driver.switch_to.window(handles[0])
# # # # sleep(1)
# # # # driver.find_element_by_link_text("Register").click()
# #
# #
# #
# #
# # # # for handle in handles[1:]:
# # # #     driver.switch_to.window(handle)
# # # #     if driver.title  == "ICICI":
# # # #         driver.close()
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # # driver.find_element_by_xpath("//button[text()='Click Me']").click()
# # # # w = WebDriverWait(driver, 10)
# # # # w.until(invisibility_of_element_located(('xpath', "//div[@style='display:Loading']")))
# # # # driver.find_element_by_name("fname").send_keys('hello')
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # def wait(func):
# # #     def wrapper(*args, **kwargs):
# # #         print('Waiting for element to be enable and visible')
# # #         sleep(3)
# # #         return func(*args, **kwargs)
# # #     return wrapper
# #
# # # @wait
# # # def enter_text(locator, *, value):
# # #     loctype, locvalue = locator
# # #     driver.find_element(loctype, locvalue).clear()
# # #     driver.find_element(loctype, locvalue).send_keys(value)
# #
# # # @wait
# # # def click_element(locator):
# # #     loctype, locvalue = locator
# # #     driver.find_element(loctype, locvalue).click()
# #
# # # @wait
# # # def select_item(locator, *, item):
# # #     loctype, locvalue = locator
# # #     lst_element = driver.find_element(loctype, locvalue)
# # #     select = Select(lst_element)
# # #     if isinstance(item, str):
# # #         select.select_by_visible_text(item)
# # #     else:
# # #         select.select_by_index(item)
# #
# # # @wait
# # # def select_items(locator, *, items):
# # #     for item in items:
# # #         try:
# # #             select_item(locator, item=item)
# # #         except NoSuchElementException:
# # #             print(f"{item} not found")
# # #             continue
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # # select_items(("id", "multiple_cars"), items=['Audi', 8, 'Maruti', 'Jaguar', 11, 'Nissan'])
# #
# # # # click_element(("xpath", "//a[text()='Register']"))
# # # # sleep(1)
# # # # click_element(("id", "gender-male"))
# # # # sleep(1)
# # # # enter_text(("name", "FirstName"), value="Hello")
# # # # sleep(1)
# # # # enter_text(("name", "LastName"), value="World")
# # # # sleep(1)
# # # # enter_text(("name", "Email"), value="Hello.world@company.com")
# # # # sleep(1)
# # # # enter_text(("name", "Password"), value="Password123")
# # # # sleep(1)
# # # # enter_text(("name", "ConfirmPassword"), value="Password123")
# #
# # # # driver.find_element('xpath', "//a[text()='Register']").click()
# # # # driver.find_element('id', "gender-male").click()
# # # # driver.find_element("name", "FirstName").send_keys("Hello")
# # # # actions = ActionChains(driver)
# # # # sleep(5)
# # # # ele = driver.find_element_by_xpath("//button[text()='Double-click me']")
# # # # actions.double_click(ele).perform()
# #
# # # # actions.send_keys(Keys.PAGE_DOWN).perform()
# #
# # # # sleep(2)
# # # # actions.send_keys(Keys.PAGE_UP).perform()
# #
# # # # actions.send_keys(Keys.TAB).perform()
# #
# #
# # # # job_search = driver.find_element_by_xpath("//a[text()='Job search']")
# # # # skills = driver.find_element_by_xpath("//a[.='Jobs by Skills']")
# # # # python_jobs = driver.find_element_by_xpath("//a[contains(text(), 'Python Jobs')]")
# #
# # # # actions.move_to_element(job_search).perform()
# # # # sleep(1)
# # # # actions.move_to_element(skills).perform()
# # # # sleep(1)
# # # # actions.move_to_element(python_jobs).perform()
# # # # sleep(1)
# # # # driver.find_element_by_xpath("//a[contains(text(), 'Python Jobs')]").click()
# # # # _xpath = "//ul[@id='header-nav-bar']//a"
# # # # _xpath_release = "(//ol[@class='list-row-container menu'])[2]//li/span[1]"
# # # # _xpath_date = "(//ol[@class='list-row-container menu'])[2]//li/span[2]"
# #
# # # # _xpath = "//table//tr/td[1]"
# # # # elements = driver.find_elements_by_xpath(_xpath)
# #
# # # # text_expected = sorted([ element.text for element in elements])
# #
# # # # driver.find_elements_by_xpath("//button[text()='Sort']")[0].click()
# #
# # # # elements = driver.find_elements_by_xpath(_xpath)
# # # # text_actual = [ element.text for element in elements]
# #
# # # # if text_expected == text_actual:
# # # #     print('PASS')
# # # # else:
# # # #     print('FAIL')
# #
# # # # _xpath_version = "(//ol[@class='list-row-container menu'])[1]//li/span[1]"
# # # # _xpath_status = "(//ol[@class='list-row-container menu'])[1]//li/span[2]"
# # # # _release_date = "(//ol[@class='list-row-container menu'])[1]//li/span[3]"
# # # # _xpath_support = "(//ol[@class='list-row-container menu'])[1]//li/span[4]"
# # # # _xpath_schedule = "(//ol[@class='list-row-container menu'])[1]//li/span[5]"
# #
# # # # driver.switch_to.frame()
# # # # versions = driver.find_elements_by_xpath(_xpath_version)
# # # # status = driver.find_elements_by_xpath(_xpath_status)
# # # # dates = driver.find_elements_by_xpath(_release_date)
# # # # support_status = driver.find_elements_by_xpath(_xpath_support)
# # # # schedule = driver.find_elements_by_xpath(_xpath_schedule)
# #
# #
# # # # for v, s, d, ss, sch in zip(versions, status, dates, support_status, schedule):
# # # #     print(v.text, '\t', s.text, '\t', d.text, '\t', ss.text, '\t', sch.text)
# # # #     sleep(1)
# #
# #
# # # # _xpath = "//td[text()='Python']/..//input[@name='download']"
# # # # _xpath = "//td[text()='iOS']/..//a[text()='Download']"
# # # # _xpath = "//a[text()='Python 3.8.1']/../..//a[text()='Release Notes']"
# # # # _xpath = "//label[text()='Good']/..//input[@type='radio']"
# #
# # # # _books = ['Science', 'Fiction', 'Health Book']
# #
# # # # for _book in _books:
# # # #     _xpath = f"//a[text()='{_book}']/../..//input[@value='Add to cart']"
# # # #     driver.find_element_by_xpath(_xpath).click()
# # # #     sleep(1)
# #
# # # # sleep(5)
# #
# # # # driver.find_element_by_xpath("//span[text()='Shopping cart']").click()
# #
# # # # sleep(3)
# #
# # # # _xpath = "(//a[text()='Science'])[2]/../..//input[@name='removefromcart']"
# #
# # # # driver.find_element_by_xpath(_xpath).click()
# #
# #
# # # # items = [
# # # #     "$25 Virtual Gift Card",
# # # #     "14.1-inch Laptop",
# # # #     "Build your own cheap computer",
# # # #     "Build your own computer",
# # # #     "Build your own expensive computer",
# # # #     "Simple Computer"
# # # #     ]
# #
# # # # prices = [25.00, 1590.00, 900.00, 1200.00, 1800.0, 800.00]
# #
# # # # d = {
# # # #     "$25 Virtual Gift Card": 25.00,
# # # #     "14.1-inch Laptop": 1590.00,
# # # #     "Build your own cheap computer": 900.00,
# # # #     "Build your own computer": 1200.00,
# # # #     "Build your own expensive computer": 1800.00,
# # # #     "Simple Computer": 800.00
# # # #     }
# #
# # # # for item, expected_price in d.items():
# # # #     _xpath = f"//a[text()='{item}']/../..//span[@class='price actual-price']"
# # # #     actual_price = driver.find_element_by_xpath(_xpath)
# # # #     if float(actual_price.text) == expected_price:
# # # #         print("PASS")
# # # #     else:
# # # #         print("FAIL")
# #
# #
# # # # element = driver.find_element_by_id("multiple_cars")
# #
# # # # s = Select(element)
# #
# # # # s.select_by_visible_text('Audi')
# # # # s.select_by_visible_text('BMW')
# # # # s.select_by_visible_text('Citroen')
# #
# # # # opt = s.first_selected_option
# #
# # # # print(opt.text)
# #
# # # # items = ["Audi", "BMW", "Citroen", "Maruti", "Mercedes", "Toyota"]
# #
# # # # for item in items:
# # # #     try:
# # # #         s.select_by_visible_text(item)
# # # #         sleep(0.5)
# # # #     except NoSuchElementException:
# # # #         print(f'{item} not found inside the list box')
# # # #         continue
# #
# # # # opts = s.options
# # # # items = [ item.text for item in opts]
# #
# # # # print(items)
# #
# # # # for item in items:
# # # #     s.select_by_visible_text(item)
# # # #     sleep(0.5)
# #
# # # # s.deselect_by_visible_text('Audi')
# #
# #
# # # # opts = s.options
# #
# # # # for index in range(1, len(opts)):
# # # #     s.select_by_index(index)
# # # #     sleep(1)
# #
# # # # items = [item.text for item in opts ]
# #
# # # # _search_car = "Audi"
# #
# # # # if _search_car in items:
# # # #     s.select_by_visible_text(_search_car)
# # # #     print(items.index(_search_car))
# #
# # # # for index, item in enumerate(items):
# # # #     if _search_car == item:
# # # #         s.select_by_visible_text(item)
# # # #         print(f'{item} is at index {index}')
# #
# #
# # # # for item in items[::-1]:
# # # #     s.select_by_visible_text(item)
# # # #     sleep(1)
# #
# # # # s.select_by_visible_text('Mercedes')
# #
# # # # sleep(1)
# #
# # # # s.select_by_visible_text('Audi')
# #
# # # # sleep(1)
# # # # s.select_by_visible_text('Jaguar')
# #
# # # # sleep(1)
# #
# # # # s.select_by_index(10)
# #
# # # # sleep(1)
# #
# # # # s.select_by_index(12)
# # # # sleep(1)
# # # # # s.select_by_index(15)
# #
# # # # ele = driver.find_element_by_name("currency")
# #
# # # # ss = Select(ele)
# #
# # # # ss.select_by_value("JPN")
# #
# # # # sleep(1)
# #
# # # # ss.select_by_index(0)
# #
# # # # sleep(1)
# #
# # # # ss.select_by_visible_text("US Dollars")
# #
# # # # print(driver.find_element_by_name('q').get_attribute("spam"))
# # # # links = driver.find_elements_by_xpath("//a")
# #
# # # # for link in links:
# # # #     if 'Python' in link.text:
# # # #         print(link.text, '--->', link.get_attribute("href"))
# # # #         sleep(0.2)
# #
# # # # names = ["Hello", "world"]
# # # # for element, name in zip(elements, names):
# # # #     element.send_keys(name)
# #
# # # # for link in links:
# # # #     if "Python" in link.text:
# # # #         print(link.text)
# #
# # # # for element in elements[::2]:
# # # #     element.click()
# # # #     sleep(1)
# #
# # # # for i in range(len(elements)-1, -1, -1):
# # # #     elements[i].click()
# # # #     sleep(1)
# #
# # # # elements[0].click()
# # # # elements[-1].click()
# #
# # # # driver.find_element_by_xpath("//a[text()='Register']").click()
# # # # sleep(1)
# # # # driver.find_element_by_xpath("//input[@id='gender-male']").click()
# # # # sleep(1)
# # # # driver.find_element_by_xpath("//input[@name='FirstName']").send_keys("Steve")
# # # # sleep(1)
# # # # driver.find_element_by_xpath("//input[@id='LastName']").send_keys("Jobs")
# # # # sleep(1)
# # # # driver.find_element_by_xpath("//input[@id='Password']").send_keys("Password123")
# # # # sleep(1)
# # # # driver.find_element_by_xpath("//input[@id='ConfirmPassword']").send_keys("Password123")
# # # # sleep(1)
# # # # driver.find_element_by_xpath("//input[@id='register-button']").click()
# #
# # # # driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys("FirstName")
# # # # sleep(1)
# # # # driver.find_element_by_xpath("/html/body/div[1]/input[2]").send_keys("LastName")
# # # # sleep(1)
# # # # driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys("Company")
# # # # sleep(1)
# # # # driver.find_element_by_xpath("/html/body/div[2]/input[2]").send_keys("Location")
# #
# # # # driver.find_element_by_css_selector("input[value='Search store']").send_keys("Computer")
# # # # driver.find_element_by_css_selector("input[value='Search']").click()
# # # # driver.find_element_by_css_selector("input[type='text']").send_keys("Hello")
# # # # driver.find_element_by_css_selector("input[type='password']").send_keys("world")
# # # # driver.find_element_by_name("spam").send_keys('hello')
# #
# # # # driver.find_element_by_partial_link_text("Inbox").click()
# #
# # # # driver.find_element_by_partial_link_text("Privacy").click()
# #
# # # # driver.find_element_by_link_text("Register").click()
# # # # sleep(4)
# # # # driver.find_element_by_id("gender-male").click()
# # # # sleep(2)
# # # # driver.find_element_by_name("FirstName").send_keys('Steve')
# # # # sleep(2)
# # # # driver.find_element_by_id("LastName").send_keys("Jobs")
# # # # sleep(2)
# # # # driver.find_element_by_id("Email").send_keys("steve.jobs@apple.com")
# # # # sleep(2)
# # # # driver.find_element_by_id("Password").send_keys("Password123")
# # # # sleep(2)
# # # # driver.find_element_by_id("ConfirmPassword").send_keys("Password123")
# # # # sleep(2)
# # # # driver.find_element_by_name("register-button").click()
