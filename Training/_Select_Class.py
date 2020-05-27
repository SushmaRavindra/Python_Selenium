from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome('/home/sandeep/Desktop/Selenium/chromedriver')

# Printing all Auto-suggestions in google search
driver.find_element_by_xpath("//input[@name='q']").send_keys("Python")
time.sleep(3)
elements = driver.find_elements_by_xpath("//div[@role='option']")

for element in elements:
    print(element.text)

# Selecting Item from Auto-Suggestion list box
driver.find_element_by_xpath("//div[text()='Select car:']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@name='myCountry']").send_keys("Uni")
time.sleep(2)
driver.find_element_by_xpath("//div[text()='ted States of America']").click()

cars = driver.find_elements_by_xpath("//select[@id='multiple_cars']")
s = Select(cars)

# Selecting Course in http://www.qspiders.com/courses auto suggest listbox

all_items = s.options
items = [item.text for item in all_items]

for item in items:
    s.select_by_visible_text(item)
    time.sleep(0.5)

# Deselecting all items from the multiple select listbox
s.select_by_visible_text("Audi")
s.select_by_visible_text("BMW")
s.deselect_all()

# Selecting Item from the Multiple Select Listbox and Printing all selected options
s.select_by_visible_text("Audi")
s.select_by_visible_text("BMW")

opts = s.all_selected_options

for item in opts:
    print(item.text)


# Searching Item inside the Listbox and Printing the index
opts = s.options
car_text = [item.text for item in opts]

for index, car in enumerate(car_text):
    if "Ford" in car:
        print('Car Found at index ', index)

driver.close()
