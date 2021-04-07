from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')

driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Progressbar.html")

driver.find_element_by_xpath("//button[text()='Click Me']").click()

# Explicit Wait or Webdriver wait
w = WebDriverWait(driver, 5, poll_frequency=2)
w.until(expected_conditions.visibility_of_element_located(("xpath", "//div[text()='50%']")))

print("Done!")

# actions = ActionChains(driver)
#
# element = driver.find_element_by_xpath("//button[text()='Double-click me']")
#
# actions.double_click(element).perform()

# actions.send_keys(Keys.PAGE_DOWN).perform()
#
# sleep(1)
#
# actions.send_keys(Keys.PAGE_DOWN).perform()
#
# sleep(1)
#
# actions.send_keys(Keys.PAGE_UP).perform()
#
# sleep(1)
#
# actions.send_keys(Keys.PAGE_UP).perform()
#
# sleep(1)
#
# actions.send_keys(Keys.ARROW_DOWN).perform()
#
# sleep(1)
#
# actions.send_keys(Keys.ARROW_DOWN).perform()
#
# sleep(1)
#
# actions.send_keys(Keys.ARROW_DOWN).perform()
#
# sleep(1)
#
# actions.send_keys(Keys.TAB).perform()
#
# sleep(1)
#
# actions.send_keys(Keys.TAB).perform()





# job_search = driver.find_element_by_xpath("//a[text()='Job search']")
#
# actions.move_to_element(job_search).perform()
#
# sleep(1)
#
# careers = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
#
# actions.move_to_element(careers).perform()




# expected_prices = {
#     "$25 Virtual Gift Card": 25.00,
#     "14.1-inch Laptop": 1590.00,
#     "Build your own cheap computer": 800.00,
#     "Build your own computer": 1200.00,
#     "Build your own expensive computer": 1800.00,
#     "Simple Computer": 700.00
# }
#
# for item, price in expected_prices.items():
#     _xpath = f"//a[text()='{item}']/../..//span[@class='price actual-price']"
#     actual_price = driver.find_element_by_xpath(_xpath).text
#     if price == float(actual_price):
#         print('PASS')
#     else:
#         print('FAIL')



# books = ["Science", "Fiction", "Health Book"]
# for book in books:
#     driver.find_element_by_xpath(f"//a[text()='{book}']/../..//input[@value='Add to cart']").click()
#     sleep(3)
#
#
# driver.find_element_by_xpath("//span[text()='Shopping cart']").click()
#
# sleep(3)
#
# quantities = [10, 20, 30]
# for quantity, book in zip(quantities, books):
#     driver.find_element_by_xpath(f"(//a[text()='{book}'])[2]/../..//input[@type='text']").clear()
#     driver.find_element_by_xpath(f"(//a[text()='{book}'])[2]/../..//input[@type='text']").send_keys(quantity)

# ele = driver.find_element_by_id("multiple_cars")
#
# s = Select(ele)
#
# opts = s.options
#
# items = [opt.text for opt in opts]
#
# for item in items:
#     s.select_by_visible_text(item)
#     sleep(0.5)
#
# s.deselect_by_visible_text("Audi")
# sleep(1)
# s.deselect_by_index(8)
# sleep(1)
# s.deselect_by_value("10")
#
# opts = s.all_selected_options
#
# for item in opts:
#     print(item.text)


# cars = ['Audi', 'Mercedes', 'Nissan', 'Honda']

# for car in cars:
#     s.select_by_visible_text(car)

# sleep(5)

# s.deselect_by_value("6")
# s.deselect_by_index(8)
# s.deselect_by_visible_text("Audi")
# s.deselect_all()

# for car in cars:
#     try:
#         s.select_by_visible_text(car)
#         sleep(1)
#     except NoSuchElementException:
#         print(f'{car} was not found!')
#         continue

# s.select_by_visible_text("Mercedes")
# sleep(1)
# print(s.first_selected_option.text)
# sleep(1)
# s.select_by_visible_text("Audi")
# print(s.first_selected_option.text)


# List Comprehension
# items = [item.text for item in opts]

# for item in items[::2]:
#     s.select_by_visible_text(item)
#     sleep(0.5)

# Get Item and Index
# for index, item in enumerate(items):
#     s.select_by_visible_text(item)
#     print(index)
#     sleep(0.5)

# car = 'Maruti'
#
# for index, item in enumerate(items):
#     if car == item:
#         print(f'{car} is at index {index}')
#         s.select_by_visible_text(item)







# s.select_by_visible_text("Mercedes")
# sleep(1)
# s.select_by_visible_text("Audi")
# sleep(1)
# s.select_by_visible_text("Honda")
# sleep(1)
# s.select_by_visible_text("Nissan")
# sleep(1)
# s.select_by_index(5)
# sleep(1)
# s.select_by_index(8)
# sleep(1)
# s.select_by_index(10)
# sleep(1)
# s.select_by_value("6")
# sleep(1)
# s.select_by_value("12")
# sleep(1)
# s.select_by_value("9")






# print(driver.find_element_by_name("q").get_attribute("spam"))

# items = driver.find_elements_by_name("spam")
#
# a = ['hello', 'world']
#
# for item, t in zip(items, a):
#     item.send_keys(t)
#     sleep(1)

# driver.find_elements_by_tag_name("a")
#
# for item in items:
#     if 'Python' in item.text:
#         print(item.text)








# driver.find_element_by_link_text("Register").click()
# driver.find_element_by_xpath("//a[text()='Register']").click()
# driver.find_element_by_xpath("(/html/body/div[4]/div/div/div[2]/div/ul/li/a)[1]").click()
# sleep(3)
#
# driver.find_element_by_id("gender-male").click()
# # driver.find_element_by_xpath("//input[@value='M']").click()
#
# sleep(1)
# driver.find_element_by_xpath("//input[@id='FirstName']").send_keys("Hello")
# # driver.find_element_by_name("FirstName").send_keys("Hello")
# sleep(1)
# driver.find_element_by_id("LastName").send_keys("world")
# sleep(1)
# driver.find_element_by_xpath("//input[@id='Email']").send_keys("a.a@aa.com")
# sleep(1)
# driver.find_element_by_name("Password").send_keys("Password123")
# sleep(1)
# driver.find_element_by_name("ConfirmPassword").send_keys("Password123")
# sleep(1)
# driver.find_element_by_name("register-button").click()




