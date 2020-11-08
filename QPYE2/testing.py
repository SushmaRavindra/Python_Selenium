from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com/")

time.sleep(5)

driver.find_element(By.LINK_TEXT, "Register").click()

driver.find_element(By.ID, "gender-male").click()

driver.find_element(By.NAME, "FirstName").send_keys("Hello")

driver.find_element(By.ID, "LastName").send_keys("world")

driver.find_element(By.ID, "Email").send_keys("a.a@company.com")

driver.find_element(By.NAME, "register-button").click()

driver.find_elements(By.NAME, "download")

# driver.find_element_by_xpath("//button[text()='Click Me']").click()
#
# w = WebDriverWait(driver, 15)
# w.until(ec.visibility_of_element_located(("xpath", "//div[text()='100%']")))
#
# print('Done!')



# time.sleep(5)
#
# driver.switch_to.frame("frame1")
#
# time.sleep(1)
#
# driver.find_element_by_xpath("//a[text()='Business']").click()
#
# driver.switch_to.default_content()
#
# driver.find_element_by_xpath("//a[text()='Google']").click()

# driver.find_element_by_xpath("//button[text()='Try it']").click()
#
# time.sleep(1)
#
# driver.switch_to.alert.dismiss()
#
# time.sleep(2)
#
# driver.find_element_by_xpath("//button[text()='Try it']").click()
#
# time.sleep(2)
#
# driver.switch_to.alert.accept()
#
# time.sleep(2)
#
# driver.find_element_by_xpath("//button[text()='Try it']").click()
#
# time.sleep(2)
#
# print(driver.switch_to.alert.text)













# driver.find_element_by_xpath("//a[text()='Twitter']").click()
#
# time.sleep(3)
#
# handles = driver.window_handles
#
# driver.switch_to.window(handles[1])
#
# time.sleep(5)
#
# driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("Hello")
#
# time.sleep(2)
#
# driver.switch_to.window(handles[0])
#
# driver.find_element_by_xpath("//a[text()='Register']").click()
#
# time.sleep(2)
#
# driver.switch_to.window(handles[1])
#
# driver.close()
#
# time.sleep(2)
#
# driver.switch_to.window(handles[0])
#
# time.sleep(2)
#
# driver.close()





# a = ActionChains(driver)
#
# register = driver.find_element_by_xpath("//a[text()='Register']")
#
# a.context_click(register).perform()

# a.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(1)
# a.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(1)
#
# a.send_keys(Keys.PAGE_UP).perform()
# time.sleep(1)
# a.send_keys(Keys.PAGE_UP).perform()
# time.sleep(1)
#
# a.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(1)
# a.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(1)
# a.send_keys(Keys.ARROW_DOWN).perform()
#
# a.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(1)
# a.send_keys(Keys.ARROW_UP).perform()
# time.sleep(1)
# a.send_keys(Keys.ARROW_UP).perform()





# btn = driver.find_element_by_xpath("//button[text()='Double-click me']")
# a.double_click(btn).perform()

# job_search = driver.find_element_by_xpath("//a[text()='Job search']")
# a.move_to_element(job_search).perform()
#
# time.sleep(2)
#
# skills = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
# a.move_to_element(skills).perform()
#
# time.sleep(2)
#
# driver.find_element_by_xpath("//a[contains(text(),'Python Jobs')]").click()








# driver.find_element_by_xpath("//td[text()='Java']/..//input[@name='download']").click()


# books = [
#          "Copy of Computing and Internet EX",
#          "Computing and Internet",
#          "Fiction",
#          "Science"
#          ]
#
# for book in books:
#     _xpath = f"//a[text()='{book}']/../..//span[@class='price actual-price']"
#     print(driver.find_element_by_xpath(_xpath).text)
#     time.sleep(1)

# boxes = driver.find_elements_by_xpath("//input[@name='download']")
#
# for box in boxes:
#     box.click()
#     time.sleep(1)



# for link in links:
#     if 'Python' in link.text:
#         print(link.text, link.get_attribute("href"))
#         time.sleep(0.5)
#
# driver.find_element_by_name("q").get_attribute("class")









# ele = driver.find_element_by_id("standard_cars")
#
# s = Select(ele)
#
# opts = s.options
#
# for index, opt in enumerate(opts):
#     if "Mercedes" == opt.text:
#         s.select_by_visible_text(opt.text)
#         print(f'{opt.text} is at index {index}')


# s.select_by_visible_text("Audi")
# time.sleep(1)
# s.select_by_visible_text("Mercedes")
# time.sleep(1)
# s.select_by_visible_text("Honda")
#
# opts = s.all_selected_options
#
# s.deselect_all()
#
# opts = s.options
#
# for opt in opts:
#     s.select_by_visible_text(opt.text)
#     time.sleep(1)

# opts = s.options
#
# s.select_by_visible_text("Honda")
#
# print(s.first_selected_option.text)

# items = []

# for opt in opts[::2]:
#     s.select_by_visible_text(opt.text)
#     time.sleep(1)














# for item in items:
#     s.select_by_visible_text(item)
#     time.sleep(1)


# s.select_by_visible_text("Honda")
#
# time.sleep(1)
#
# s.select_by_index(8)















# driver.find_element_by_link_text("Log in").click()
#
# time.sleep(2)
#
# driver.find_element_by_id("Email").send_keys("bill.gates@company.com")
#
# time.sleep(2)
#
# driver.find_element_by_name("Password").send_keys("Password")
# time.sleep(2)
#
# driver.find_element_by_xpath("//input[@value='Log in']").click()
#
# time.sleep(2)
#
# result = driver.find_element_by_xpath("//li[text()='The credentials provided are incorrect']").is_displayed()
# # result = driver.find_element_by_link_text("bill.gates@company.com").is_displayed()
#
#
# if result == True:
#     print('Login Failure')
# else:
#     print('Login Success')
















# driver.find_element_by_link_text("Register").click()
#
# time.sleep(2)
#
# driver.find_element_by_id("gender-male").click()
#
# time.sleep(2)
#
# driver.find_element_by_id("FirstName").send_keys("Hello")
#
# time.sleep(2)
#
# driver.find_element_by_name("LastName").send_keys("World")
#
# time.sleep(2)
#
# driver.find_element_by_name("Email").send_keys("Hello.World@gmail.com")
#
# time.sleep(2)
#
# driver.find_element_by_id("Password").send_keys("admin")
#
# time.sleep(2)
#
# driver.find_element_by_id("ConfirmPassword").send_keys("admin")
#
# time.sleep(2)
#
# driver.find_element_by_id("register-button").click()
#
# time.sleep(2)
#
# driver.close()
