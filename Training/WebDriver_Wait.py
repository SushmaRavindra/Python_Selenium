from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome('/home/sandeep/Desktop/Selenium/chromedriver')
driver.get("file:///home/sandeep/Desktop/Selenium/HTML_Pages/Loading.html")

txt_middle_name = driver.find_element_by_name("mname")

wait = WebDriverWait(driver, timeout=10)

# Visibility_of (Wait until element is visible on the webpage, But the webelement should be present on the DOM)
# If the webelment is not present on the DOM, then it will throw NoSuchElementException
wait.until(ec.visibility_of(txt_middle_name))

# Visibility_of_element_located (Waits until the element is loaded in DOM and also visible on the webpage)
wait.until(ec.visibility_of_element_located(("name", "mname")), message="Element failed to load with in timeout period of 10 seconds")

txt_middle_name.send_keys("Hello")

driver.close()
