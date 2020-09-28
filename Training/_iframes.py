from selenium import webdriver
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait


# driver.get("https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Other_embedding_technologies")
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.moneycontrol.com/")
element = driver.find_element_by_xpath("(//iframe)[1]")
driver.switch_to.frame(element)
driver.find_element_by_xpath("(//a[text()='Nifty 50'])[1]").click()
# element = driver.find_element_by_xpath("//a[@id='header-signin-link']")
# element.click()
# driver.refresh()
# element.click()
# headers = driver.find_elements_by_xpath("(//table[@class='mctable1'])[1]//th")
# data = driver.find_elements_by_xpath("(//table[@class='mctable1'])[1]//tbody/tr//td")
# rows = driver.find_elements_by_xpath("(//table[@class='mctable1'])[1]//tr")
# hds = [header.text for header in headers]
# row = driver.find_elements_by_xpath("(//a[text()='NIFTY 50'])[2]/../..//td")
#
# companies = ['SENSEX', 'NIFTY 50']
#
# for company in companies:
#     _xpath = f"(//a[text()='{company}'])[2]/../..//td"
#     row = driver.find_elements_by_xpath(_xpath)
#     for td in row:
#         print(td.text, end='')
#     print()










# firefoxProfile = webdriver.FirefoxProfile()
# firefoxProfile.set_preference("dom.webnotifications.enabled", False)
# driver = webdriver.Firefox(options=firefoxProfile)
# driver.get("https://www.redbus.in/")

# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument("--disable-notifications")
# driver = webdriver.Chrome('./chromedriver', options=chromeOptions)
# driver.get("https://www.redbus.in/")



# element = driver.find_element_by_xpath("(//iframe)[8]")
# driver.switch_to.frame(element)
# headers = driver.find_elements_by_xpath("//table[@class='ind-mp_tbl sortable']//th")
# states = driver.find_elements_by_xpath("//table[@class='ind-mp_tbl sortable']//tr/td[1]")
#
# for header in headers:
#     print(f'{header.text:>15}', end='')
#
# print()
#
# for state in states:
#     _xpath = f"//td[text()='{state.text}']/..//td/p[@class='mid-wrap']"
#     data = driver.find_elements_by_xpath(_xpath)
#     for row in data:
#         print(row.text, end='')
#     print()












# table = driver.find_element_by_xpath("(//iframe)[9]")
# driver.switch_to.frame(table)
# driver.find_element_by_xpath("//table[@class='ind-mp_tbl sortable']")

# Get Headers
# headers = driver.find_elements_by_xpath("//table[@class='ind-mp_tbl sortable']//th")
# for header in headers:
#     print(f'{header.text:>10}', end='')
# print()

# rows = driver.find_elements_by_xpath("//table[@class='ind-mp_tbl sortable']/tbody/tr")
# cols = driver.find_elements_by_xpath("//table[@class='ind-mp_tbl sortable']/tbody//tr[1]//p[@class='mid-wrap']")


# for col in cols:
#     print(f'{col.text:>10}', end='')

# driver.find_element_by_xpath("//textarea[@id='code']").send_keys("Hello world")

# driver.find_element_by_xpath("(//span[text()='Bedsheets, curtains & more'])[1]").click()
# Either you can use name or id or index or iframe element
# driver.find_element_by_xpath("//a[text()='Google']").click()

# element = driver.find_element_by_xpath("//iframe[@name='frame1']")
# driver.switch_to.frame(element)
# sleep(1)
# driver.find_element_by_xpath("//a[text()='Business']").click()
# sleep(2)
# # Switch the driver control from frame to main webpage/default content
# driver.switch_to.default_content()
# sleep(1)
# driver.find_element_by_xpath("//a[text()='Google']").click()
# element = driver.find_element_by_xpath("//iframe[@id='LOTCCFrame_1600829183262']")
# driver.switch_to.frame(element)
# sleep(2)
# print(driver.find_element_by_xpath("//div[@id='buttons']").get_attribute("class"))