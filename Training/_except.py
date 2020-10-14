from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/books")

element = driver.find_element_by_name("q")
element.send_keys("Computer")

print(element)

driver.refresh()

sleep(2)

element = driver.find_element_by_name("q")

print(element)

element.send_keys("iphone")


# element = driver.find_element_by_id("products-orderby")
#
# print(element)
#
# s = Select(element)
#
# s.select_by_visible_text("Created on")
#
# sleep(2)
#
# element = driver.find_element_by_id("products-orderby")
#
# print(element)
#
# s = Select(element)
#
# s.select_by_visible_text("Price: Low to High")
