from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.myntra.com/')
sleep(5)

driver.find_element_by_xpath("//input[@class='desktop-searchBar']").send_keys("nike")
sleep(2)
driver.find_element_by_xpath("//li[text()='Nike Shoes']").click()




# for e in ele:
#     e.click()
# driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys("nike")
# sleep(5)
# driver.find_element_by_xpath("//li[text()='Nike Shoes']").click()
