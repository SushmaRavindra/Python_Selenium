from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Autocomplete_list.html")
sleep(5)

# driver.find_element_by_xpath("//div[@class='select-selected']").click()
# sleep(1)
# driver.find_element_by_xpath("//div[text()='Honda']").click()

driver.find_element_by_name("myCountry").send_keys("Un")
sleep(1)
driver.find_element_by_xpath("//div[text()='ited Kingdom']").click()