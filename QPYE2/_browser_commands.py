from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import xlrd


def read_locators(pagename):
    wb = xlrd.open_workbook("Objects.xlsx")
    ws = wb.sheet_by_name(pagename)
    rows = ws.get_rows()
    next(rows)    # Skip headers
    return {row[0].value: (row[1].value, row[2].value) for row in rows}


d = read_locators("RegistrationPage")

print(d)


# class Objects:
#     def __init__(self, lname, loctype, locvalue):
#         self.lname = lname
#         self.loctype = loctype
#         self.locvalue = locvalue
#
# LoginPageObjects = []
# rows = ws.get_rows()
# for row in rows:
#     LoginPageObjects.append(Objects(row[0].value, row[1].value, row[2].value))
#
# for item in LoginPageObjects:
#     print(item.lname, item.loctype, item.locvalue)




# d = {
#     "txt_email": ("name", "Email"),
#     "txt_password": ("name", "Password"),
#     "btn_login": ("xpath", "//input[@value='Log in']")
#  }


portfolio = []

def to_dict(row):
    return dict(zip(['name', 'shares', 'price'],
                    [row[0].value, row[1].value, row[2].value]))

for row in rows:
    portfolio.append(
        {
        "name": row[0].value,
        "shares": row[1].value,
        "price": row[2].value
    })

for item in portfolio:
    if item['price'] > 2000:
        print(item)

print(sorted(portfolio, key=lambda item: item['shares']))

total = 0.00

for item in portfolio:
    total += item['price']

print(total)






















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


