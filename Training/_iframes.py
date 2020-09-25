from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
# driver.get("https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Other_embedding_technologies")
driver.get("https://www.ndtv.com/")
sleep(10)

element = driver.find_element_by_xpath("(//iframe)[8]")
driver.switch_to.frame(element)
headers = driver.find_elements_by_xpath("//table[@class='ind-mp_tbl sortable']//th")
states = driver.find_elements_by_xpath("//table[@class='ind-mp_tbl sortable']//tr/td[1]")

for header in headers:
    print(f'{header.text:>15}', end='')

print()

for state in states:
    _xpath = f"//td[text()='{state.text}']/..//td/p[@class='mid-wrap']"
    data = driver.find_elements_by_xpath(_xpath)
    for row in data:
        print(row.text, end='')
    print()












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