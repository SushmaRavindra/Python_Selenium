from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome('./chromedriver')
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
sleep(5)

# Double Click on Custom HTML Page
action = ActionChains(driver)
btn = driver.find_element_by_xpath("//button[text()='Double-click me']")
action.double_click(btn).perform()

# Right Click or Context click
action = ActionChains(driver)
lnk_register = driver.find_element_by_xpath("//span[text()='right click me']")
action.context_click(lnk_register).perform()
driver.find_element_by_xpath("//span[text()='Cut']").click()

# about = driver.find_element_by_xpath("//a[text()='About']")
# action.move_to_element(about).perform()
# sleep(1)
#
# blog = driver.find_element_by_xpath("//a[text()='Blog']")
# action.move_to_element(blog).perform()
#
# projects = driver.find_element_by_xpath("//a[text()='Projects']")
# action.move_to_element(projects).perform()
# sleep(1)
#
# contacts = driver.find_element_by_xpath("//a[text()='Contact']")
# action.move_to_element(contacts).perform()
# sleep(1)
#
# # Improved Version
# _menus = ['Contact', 'Projects', 'Blog', 'About']
# for _menu in _menus[::-1]:
#     _xpath = f"//a[text()='{_menu}']"
#     about = driver.find_element_by_xpath(_xpath)
#     print(_menu)
#     action.move_to_element(about).perform()
#     sleep(1)
#
#
# driver.find_element_by_name("q").send_keys("Computer")
# sleep(2)
# action.send_keys(Keys.TAB).perform()
# sleep(1)
# action.send_keys(Keys.ENTER).perform()
#
# action.send_keys(Keys.PAGE_DOWN).perform()
# sleep(1)
# action.send_keys(Keys.PAGE_UP).perform()
#
# action.send_keys(Keys.ARROW_DOWN).perform()
# sleep(1)
# action.send_keys(Keys.ARROW_DOWN).perform()
# sleep(1)
# action.send_keys(Keys.ARROW_DOWN).perform()
# sleep(1)
# action.send_keys(Keys.ARROW_DOWN).perform()
# sleep(1)
# action.send_keys(Keys.ARROW_UP).perform()
# sleep(1)
# action.send_keys(Keys.ARROW_UP).perform()
# sleep(1)
# action.send_keys(Keys.ARROW_UP).perform()
#
# # Mouse Hover on Menu item (Karnataka) in Qspiders.com and click on "Mysore"
# state = driver.find_element_by_xpath("//span[text()='Karnataka']")
# action.move_to_element(state).perform()
# sleep(1)
# driver.find_element_by_xpath("//a[text()='Mysore']").click()
#
# # Mouse Hover on Multiple Menu's on Custom HTML page
# about = driver.find_element_by_xpath("//button[text()='About ']")
# action.move_to_element(about)
# sleep(1)
# careers = driver.find_element_by_xpath("//a[text()='Careers']")
# action.move_to_element(careers)
# action.click().perform()
