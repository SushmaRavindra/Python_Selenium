from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Javascript_Alert.html")
sleep(5)

# driver.find_element_by_xpath("//button[text()='Try it']").click()

# sleep(1)
driver.switch_to.alert.dismiss()
