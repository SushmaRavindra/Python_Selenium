from selenium import webdriver
import time
import csv
import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest

driver = webdriver.Chrome('/home/sandeep/Desktop/Selenium/chromedriver')
# driver = webdriver.Chrome(options=opts)
# driver.get("http://demowebshop.tricentis.com/books?orderby=6")
# driver.get("https://www.ndtv.com/")
# driver.get("http://www.qspiders.com/")
# driver.get("http://naukri.com/")
# driver.get("http://demowebshop.tricentis.com/")
# driver.get("http://demowebshop.tricentis.com/books")
# driver.get("file:///home/sandeep/Desktop/Selenium/HTML_Pages/Table_Sorting.html")
# driver.get("https://www.seleniumeasy.com/test/bootstrap-download-progress-demo.html")
# _loading = "//div[text()=' loading...']"
# _progress = "//div[text()='100%']"
# wait = WebDriverWait(driver, timeout=25)
# wait.until(ec.visibility_of_element_located(("xpath", _progress)))
# driver.close()



driver.get("http://google.com")
driver.get("http://yahoo.com")
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
driver.maximize_window()

# for win in win_handles:
#     driver.switch_to.window(win)
#     print(driver.title)
#     time.sleep(1)

# for win in reversed(win_handles):
#     driver.switch_to.window(win)
#     driver.close()
#     time.sleep(1)