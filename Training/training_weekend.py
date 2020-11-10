from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.google.com/")

sleep(3)

expected_title = "Google"

actual_title = driver.title

if expected_title == actual_title:
    print('PASS')
else:
    print('FAIL')

driver.refresh()
driver.forward()
driver.back()
driver.current_url

driver.quit()
