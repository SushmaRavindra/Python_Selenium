from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com/")

time.sleep(3)

driver.find_element_by_xpath("//a[text()='Register']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@value='M']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@name='FirstName']").send_keys("Sandeep")
time.sleep(1)
driver.find_element_by_xpath("//input[@id='LastName']").send_keys("Suryaprasad")
time.sleep(1)
driver.find_element_by_xpath("//input[@class='button-1 register-next-step-button']").click()

driver.find_element_by_xpath("//input[@name='NewsletterEmail']").send_keys("abc@abc.com")
for index in range(1, 5):
    _xpath = f"//input[@id='pollanswers-{index}']"
    driver.find_element_by_xpath(_xpath).click()
    driver.find_element_by_xpath("//input[@value='Vote']").click()


# General Form of CSS Selector
# HTMLTAG[Property=value]

# General form for xpath
# HTML[@property=value]

driver.find_element_by_css_selector("input[type='text']").send_keys("Sandeep")
driver.find_element_by_css_selector("input[type='password']").send_keys("Password123")


driver.find_element_by_link_text("Register").click()

time.sleep(1)

driver.find_element_by_id("gender-male").click()

time.sleep(1)

driver.find_element_by_name("FirstName").send_keys("Sandeep")

time.sleep(1)

driver.find_element_by_id("LastName").send_keys("Suryaprasad")

time.sleep(1)

driver.find_element_by_name("register-button").click()
