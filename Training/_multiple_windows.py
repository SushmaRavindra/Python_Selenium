from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/")
sleep(5)

wins = driver.window_handles

# Closing all child browsers
for win in win_handles[1:]:
    driver.switch_to.window(win)
    driver.close()
    sleep(1)

# Closing all Browsers including Parent browser
for win in wins:
    driver.switch_to.window(win)
    driver.close()
    sleep(1)

# Closing all Browsers in reversed order
for win in reversed(wins):
    driver.switch_to.window(win)
    driver.close()
    sleep(1)

# Closing all Browsers in reversed order using Slicing syntax
for win in wins[::-1]:
    driver.switch_to.window(win)
    driver.close()
    sleep(1)

# Print the title of all the windows of naukri.com
for win in wins:
    driver.switch_to.window(win)
    print(driver.title)
    sleep(1)

# Close the browser which has title Amazon/HSBC in naukri.com
for win in wins:
    driver.switch_to.window(win)
    _title = driver.title
    if _title == 'HSBC':
        driver.close()

# Open Demo webshop, click on Facebook link and then enter username and pwd in facebook login page

driver.find_element_by_xpath("//a[text()='Facebook']").click()
sleep(1)
wins = driver.window_handles
driver.switch_to.window(wins[1])
driver.find_element_by_name("email").send_keys("Hello")
sleep(2)
driver.find_element_by_name("pass").send_keys("world")
sleep(2)
driver.close()
# Switch back to parent window
driver.switch_to.window(wins[0])
sleep(2)
driver.find_element_by_xpath("//a[text()='Register']").click()
