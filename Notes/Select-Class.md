### Exercise :1
**Selecting item from a standard listbox**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.get("file:///HTML_Pages/Standard_listbox.html")

time.sleep(2)

lst_cars = driver.find_element_by_id("standard_cars")

# Create instance of Select class and pass the WebElement (last_cars) as constructor arguments
select = Select(lst_cars)

# Selecting item by visible text
select.select_by_visible_text("Honda")
time.sleep(2)

# Selecting item by index
select.select_by_index(8)   # Selects the item at index 8
time.sleep(2)

# Selecting item by value
select.select_by_value('11')    # Selects the item with value 11
time.sleep(3)

driver.quit()
```
### Exercise :2
**Selecting day, month and year in Facebook.com**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.facebook.com/")
time.sleep(3)


bday = driver.find_element_by_name("birthday_day")
b_day = Select(bday)
b_day.select_by_visible_text("10")

time.sleep(1)

bmonth = driver.find_element_by_name("birthday_month")
b_month = Select(bmonth)
b_month.select_by_visible_text("Aug")

time.sleep(1)

byear = driver.find_element_by_name("birthday_year")
b_year = Select(byear)
b_year.select_by_visible_text("1995")
```
### Exercise :3

```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.get('http://demowebshop.tricentis.com/books')

time.sleep(2)

lst_sort_by = driver.find_element_by_id("products-orderby")

select = Select(lst_sort_by)

# Selecting item by visible text
select.select_by_visible_text("Name: A to Z")

time.sleep(3)

# Selecting item by index
select.select_by_index(4)   # Selects the item at index-4 (Price: High to Low)

time.sleep(3)
driver.quit()
```
When the above code is executed StaleElementReferenceException is raised. Because, when the first item is selected from the list box, the entire page gets refreshed and all the DOM elements would have deleted and reloaded back in the DOM. So the reference to the list box would have lost by the variable "lst_sort_by". It would be referring to the older referenceID. But Selenium would have created a new referenceID for the list box.

* ID Before Refresh:  <selenium.webdriver.remote.webelement.WebElement (session="8a3331b1c606bc1c78cb76528185dc8b", element="d70bec9b-7ac2-4265-beab-bfccfdee382e")>
* ID After Refresh:  <selenium.webdriver.remote.webelement.WebElement (session="8a3331b1c606bc1c78cb76528185dc8b", element="0998e2c8-0074-436a-9bbd-e4222650d4bf")>

```python
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
  (Session info: chrome=84.0.4147.89)
```

**Code to handle StaleElementReferenceException**

```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
import time

# Instantiate a Chrome Browser
chrome_driver_path = "/users/sandeep/documents/Python_Selenium/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()

driver.get('http://demowebshop.tricentis.com/books')
time.sleep(2)
lst_sort_by = driver.find_element_by_id("products-orderby")
select = Select(lst_sort_by)

# Selecting item by visible text
select.select_by_visible_text("Name: A to Z")
time.sleep(3)

try:
    # Selecting item by index
    select.select_by_index(4)   # Selects the item at index-4 (Price: High to Low)
except StaleElementReferenceException:
    lst_sort_by = driver.find_element_by_id("products-orderby")
    select = Select(lst_sort_by)
    select.select_by_index(4)

time.sleep(3)

driver.quit()
```
### Exercise :4
**Print the text of all the items present in the listbox**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
driver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///Users/HTML_Pages/Standard_listbox.html')
time.sleep(2)

lst_cars = driver.find_element_by_id("standard_cars")
cars = Select(lst_cars)

# Get all the options from the listbox
opts = cars.options
for item in opts:
    print(item.text)

time.sleep(2)
driver.quit()
```
### Exercise :5
**Selecting the items in the listbox in reversed order**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///Users/HTML_Pages/Standard_listbox.html')
time.sleep(2)

lst_cars = driver.find_element_by_id("standard_cars")
cars = Select(lst_cars)

# Get the list of all the options present in the listbox.
opts = cars.options 

# Get the text of all elements to a list.
items = [item.text for item in opts]  

# Iterate through the list in reversed order.
for item in reversed(items):
    cars.select_by_visible_text(item)
    time.sleep(1)

time.sleep(2)

driver.quit()
```
**Alternate Solution (using Slicing syntax)**
```python
for item in items[::-1]:
    cars.select_by_visible_text(item)
    time.sleep(1)
```
### Exercise :6
**Selecting items in the listbox one-by-one using index.**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///HTML_Pages/Standard_listbox.html')
time.sleep(2)

lst_cars = driver.find_element_by_id("standard_cars")
cars = Select(lst_cars)

opts = cars.options

for index, item in enumerate(opts):
    cars.select_by_index(index)
    time.sleep(1)

time.sleep(2)
driver.quit()
``` 
### Exercise :7
**Selecting items in the listbox one-by-one using index in reversed order.**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/HTML_Pages/Standard_listbox.html")
time.sleep(3)

cars = driver.find_element_by_id("standard_cars")

select = Select(cars)
opts = select.options

for i in range(len(opts)-1, -1, -1):
    select.select_by_index(i)
    time.sleep(1)
```
### Exercise :8
**Check if a particular item is present in the listbox. If the item in present, then print the index at which that item is located.**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///HTML_Pages/Standard_listbox.html')
time.sleep(2)

lst_cars = driver.find_element_by_id("standard_cars")
cars = Select(lst_cars)

opts = cars.options
items = [item.text for item in opts]

# Check if the particular car is present in the list
for index, item in enumerate(items):
  if 'BMW' == item:
     print(f'{item} is present at the index {index}')

time.sleep(2)
driver.quit()
```
### Exercise :9
**Print the item which is currently selected in the listbox.**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///HTML_Pages/Standard_listbox.html')
time.sleep(2)

lst_cars = driver.find_element_by_id("standard_cars")
cars = Select(lst_cars)

cars.select_by_visible_text('BMW')

time.sleep(2)

print(cars.first_selected_option.text)

time.sleep(2)
driver.quit()
```
### Exercise :10
**Selecting multiple items from the multi-select listbox**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///TML_Pages/Standard_listbox.html')
time.sleep(2)

lst_cars = driver.find_element_by_id("multiple_cars")
cars = Select(lst_cars)

cars.select_by_visible_text('BMW')
time.sleep(1)
cars.select_by_visible_text('Audi')
time.sleep(1)
cars.select_by_visible_text('Ford')

time.sleep(2)
driver.quit()
```
### Exercise :11
**Prints all the selected items in the multi-select listbox**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
chrome_driver_path = "/users/sandeep/documents/Python_Selenium/chromedriver"
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///HTML_Pages/Standard_listbox.html')
time.sleep(2)

lst_cars = driver.find_element_by_id("multiple_cars")
cars = Select(lst_cars)

cars.select_by_visible_text('BMW')
time.sleep(1)
cars.select_by_visible_text('Audi')
time.sleep(1)
cars.select_by_visible_text('Ford')

all_opts = cars.all_selected_options
for item in all_opts:
    print(item.text)


time.sleep(2)
driver.quit()
```
### Exercise :12
**De-selecting items from multi-select listbox**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get('file:///HTML_Pages/Standard_listbox.html')
time.sleep(2)

lst_cars = driver.find_element_by_id("multiple_cars")
cars = Select(lst_cars)

# Select few items
cars.select_by_visible_text('BMW')
time.sleep(1)
cars.select_by_visible_text('Audi')
time.sleep(1)

# De-Select by visible text
cars.deselect_by_visible_text('BMW')

time.sleep(2)

# De-Select by index
cars.deselect_by_index(1)

time.sleep(3)
driver.quit()
```
### Exercise :13
**Selecting all the items of the multi-select listbox**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///HTML_Pages/Standard_listbox.html')
time.sleep(2)

lst_cars = driver.find_element_by_id("multiple_cars")
cars = Select(lst_cars)

opts = cars.options

for item in opts:
    t = item.text
    cars.select_by_visible_text(t)

time.sleep(3)
driver.quit()
```
### Exercise :14
**Print the index and item name of all the selected items in multi-select listbox**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# Instantiate a Chrome Browser
chrome_driver_path = "/users/sandeep/documents/Python_Selenium/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get('file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Standard_listbox.html')
time.sleep(2)

lst_cars = driver.find_element_by_id("multiple_cars")
cars = Select(lst_cars)

cars.select_by_visible_text("Audi")
cars.select_by_visible_text("BMW")
cars.select_by_visible_text("Ford")

for index, item in enumerate(cars.all_selected_options):
    print(index, item.text)

time.sleep(3)
driver.quit()
```
### Exercise :15
**Script to display the count of items present in the listbox**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/HTML_Pages/Standard_listbox.html")
time.sleep(3)

lst_car = driver.find_element_by_id("standard_cars")
cars = Select(lst_car)
opts = cars.options

print(len(opts))
```
### Exercise :16
**How to verify programatically if the given listbox is multi-select or single-select**
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Standard_listbox.html")
time.sleep(3)

lst_box = driver.find_element_by_xpath("//select[@id='standard_cars']")
s = Select(lst_box)

print(s.is_multiple)      # Returns False
```
```python
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Standard_listbox.html")
time.sleep(3)

lst_box = driver.find_element_by_xpath("//select[@id='multiple_cars']")
s = Select(lst_box)

print(s.is_multiple)      # Returns True
```

### Auto Suggestion Listbox
### Exercise :1
```python
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.myntra.com/')
sleep(5)

driver.find_element_by_xpath("//input[@class='desktop-searchBar']").send_keys("nike")
sleep(2)
driver.find_element_by_xpath("//li[text()='Nike Shoes']").click()
```
### Exercise :2
```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.monsterindia.com/")
sleep(5)

driver.find_element_by_xpath("//input[@placeholder='Search by Skills, Company & Job Title']").send_keys("Python Automation")



```