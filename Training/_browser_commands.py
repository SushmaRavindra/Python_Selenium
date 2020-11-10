from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import xlrd

wb = xlrd.open_workbook("TestData.xlsx")
ws = wb.sheet_by_name("Shopping")
rows = ws.get_rows()


for index, row in enumerate(rows):
    if not row[0].value == "test_shopping":
        continue
    data = ws.row_values(index-1, start_colx=2)
    print(data)
    headers = ','.join([item for item in data if item])
    print(headers)
    break

rows = ws.get_rows()

final_data = []
for index, row in enumerate(rows):
    if row[0].value == "test_shopping":
        temp = ws.row_values(index, start_colx=1)
        data = [item for item in temp if item]
        if data[0] == "Yes":
            final_data.append(tuple(data[1:]))

for item in final_data:
    print(item)










# def read_locators(pagename):
#     wb = xlrd.open_workbook("Objects.xlsx")
#     ws = wb.sheet_by_name(pagename)
#     rows = ws.get_rows()
#     next(rows)    # Skip headers
#     return {row[0].value: (row[1].value, row[2].value) for row in rows}
#
#
# d = read_locators("RegistrationPage")
#
# print(d)















# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("prefs", {"download.default_directory": r"/users/sandeep/documents",
#                                     "safebrowsing.enabled": True})

# driver = webdriver.Chrome('./chromedriver')
# driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/iframe.html")
# sleep(5)
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='frame1']"))
#
# driver.find_element_by_xpath("//a[text()='Business']").click()
#
# driver.switch_to.default_content()
#
# driver.find_element_by_xpath("//a[text()='Google']").click()



# driver.switch_to.frame("frame1")
# sleep(2)
# driver.find_element_by_xpath("//a[text()='Business']").click()
# driver.switch_to.parent_frame()
# driver.find_element_by_xpath("//a[text()='Google']").click()




















# driver.find_element_by_xpath("//input[@placeholder='Search by Skills, Company & Job Title']").send_keys("Python Automation")
#
# sleep(2)
#
# driver.find_element_by_xpath("//strong[text()='Python Automation']").click()
# actions = ActionChains(driver)
# job_search = driver.find_element_by_xpath("//a[text()='Job search']")
#
# # Mouse Hover on Job Search link
# actions.move_to_element(job_search).perform()
#
# jobs_by_skills = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
#
# # Mouse Hover on Jobs By Skills link
# actions.move_to_element(jobs_by_skills).perform()
#
# # Click on Python Jobs link
# driver.find_element_by_xpath("//a[contains(text(),'Python Jobs')]").click()





# driver.find_element_by_xpath("//button[text()='Try it']").click()
# print(driver.switch_to.alert.text)


# driver.find_element_by_xpath("//input[@name='keyword']").send_keys("Python")
#
# driver.find_element_by_xpath("//button[text()='Search']").click()
#
# driver.find_element_by_xpath("//a[@class='title fw500 ellipsis']").click()
#
# handles = driver.window_handles

# driver.switch_to.window(handles[1])

# driver.find_element_by_xpath("//a[@title='Share on Facebook']").click()

# handles = driver.window_handles

# for handle in handles:
#     driver.switch_to.window(handle)
#     print(driver.title)

# sites = ["Twitter", "Facebook", "YouTube"]
#
# for site in sites:
#     driver.find_element_by_xpath(f"//a[text()='{site}']").click()
#     sleep(1)

# Win handles of all the windows









# for handle in reversed(handles):
#     driver.switch_to.window(handle)
#     driver.close()
#     sleep(1)



# driver.find_element_by_xpath("//input[@name='location']").send_keys("Bangalore")
# sleep(2)
#
# a = ActionChains(driver)
# a.send_keys(Keys.ARROW_DOWN)
# a.send_keys(Keys.ARROW_DOWN)
# sleep(2)
# a.send_keys(Keys.ENTER)
# a.perform()

# driver.find_element_by_xpath("//div[text()='Sector 2 HSR Layout - Bengaluru/Bangalore']").click()

# driver.find_element_by_xpath("//input[@name='keyword']").send_keys("Python")
#
# sleep(1)
#
# driver.find_element_by_xpath("//button[text()='Search']").click()
#
# sleep(5)
#
# titles = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
#
# for title in titles:
#     print(title.text)

# actions = ActionChains(driver)
#
# ele = driver.find_element_by_xpath("//a[text()='Job search']")
#
# actions.move_to_element(ele)
#
# sleep(1)
#
# jobs_skills = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
#
# sleep(1)
#
# actions.move_to_element(jobs_skills)
#
# actions.perform()
#
# sleep(1)
#
# driver.find_element_by_xpath("//a[contains(text(), 'Python Jobs')]").click()


