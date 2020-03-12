from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/sandeep/Desktop/Selenium/chromedriver')
# driver.get("http://demowebshop.tricentis.com/")
# driver.get("https://www.ndtv.com/")
# driver.get("http://www.qspiders.com/")

driver.get("file:///home/sandeep/Desktop/Selenium/HTML_Pages/Tables.html")

driver.maximize_window()


actions = ActionChains(driver)

actions.send_keys(Keys.PAGE_DOWN).perform()

actions.send_keys(Keys.PAGE_DOWN).perform()

actions.send_keys(Keys.TAB).perform()

time.sleep(1)

actions.send_keys(Keys.TAB).perform()

time.sleep(1)

actions.send_keys(Keys.ENTER).perform()

time.sleep(1)

actions.send_keys(Keys.ARROW_DOWN).perform()


gallery = driver.find_element_by_xpath("//a[text()='Gallery ']")
placements = driver.find_element_by_xpath("(//a[text()='Placements'])[2]")

actions = ActionChains(driver)

actions.move_to_element(gallery).perform()

time.sleep(1)

actions.move_to_element(placements).perform()

placements.click()

actions.move_to_element(driver.find_element_by_xpath(_about)).perform()

time.sleep(1)

actions.move_to_element(driver.find_element_by_xpath(_careers)).perform()

time.sleep(1)

driver.find_element_by_xpath(_careers).click()

_about = "//a[text()='About']"
_blog = "//a[text()='Blog']"
_projects = "//a[text()='Projects']"
_contacts = "//a[text()='Contact']"

menus = ["About", "Blog", "Projects", "Contact"]
for item in menus:
    element = driver.find_element_by_xpath(f"//a[text()='{item}']")
    actions.move_to_element(element).perform()
    time.sleep(1)