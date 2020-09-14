from selenium import webdriver
import time


driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Tables.html")
time.sleep(2)
driver.find_element_by_xpath("//td[text()='Python']/..//input[@name='download']").click()