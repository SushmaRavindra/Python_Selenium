from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("./chromedriver")

driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Xpath.html")

driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys("Hello")
sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/input[2]").send_keys("Hello")
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys("Company")
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/input[2]").send_keys("Location")

import csv

w = csv.writer()
w.w
