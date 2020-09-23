from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.amazon.in/")
sleep(5)

driver.find_element_by_xpath("(//span[text()='Bedsheets, curtains & more'])[1]").click()
# Either you can use name or id or index or iframe element
driver.find_element_by_xpath("//a[text()='Google']").click()

element = driver.find_element_by_xpath("//iframe[@name='frame1']")
driver.switch_to.frame(element)
sleep(1)
driver.find_element_by_xpath("//a[text()='Business']").click()
sleep(2)
# # Switch the driver control from frame to main webpage/default content
# driver.switch_to.default_content()
# sleep(1)
# driver.find_element_by_xpath("//a[text()='Google']").click()
# element = driver.find_element_by_xpath("//iframe[@id='LOTCCFrame_1600829183262']")
# driver.switch_to.frame(element)
# sleep(2)
# print(driver.find_element_by_xpath("//div[@id='buttons']").get_attribute("class"))