from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Safari()
driver.get('http://google.com')
driver.maximize_window()

driver.quit()