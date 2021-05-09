### Exercise 1:
**Write a script to select the checkbox (in custom HTML page) corresponding to the languages mentioned in the list.**
```python
from selenium import webdriver
import time


driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Tables.html")
time.sleep(2)

_languages = ['Python', 'Java', 'JavaScript']

for _language in _languages:
    _xpath = f"//td[text()='{_language}']/..//input[@name='download']"
    driver.find_element_by_xpath(_xpath).click()
    time.sleep(1)

```
### Exercise 2:
**Write a script to select different voting radio buttons in demo webshop page**

```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Tables.html")
time.sleep(2)

_votes = ['Good', 'Excellent', 'Poor']

for _vote in _votes:
    _xpath = f"//label[text()='{_vote}']/..//input[@type='radio']"
    driver.find_element_by_xpath(_xpath).click()
    time.sleep(1)
```

### Exercise 3:
**Write a script to print link text of download link of different python releases**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.python.org")
time.sleep(2)

_releases = ['Python 3.7.8', 'Python 3.8.3', 'Python 2.7.17']

for _release in _releases:
    _xpath = f"//a[text()='{_release}']/../..//a[text()=' Download']"
    print(driver.find_element_by_xpath(_xpath).text)
    time.sleep(1)
```
### Exercise 4:

**Write a script to get the price tag of different gadgets in demo webshop and validate the actual price with pre-defined prices**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/books")
time.sleep(2)

price_tag = {
             "$25 Virtual Gift Card": 25.00,
             '14.1-inch Laptop': 1590.00,
             'Build your own cheap computer': 800.00,
             'Simple Computer': 800.00,
             'Build your own expensive computer': 1800.00,
             'Build your own computer': 1200.00
             }

for _item, _expected_price in price_tag.items():
    print(f'Validating Price of {_item}: ', end='')
    _xpath = f"//a[text()='{_item}']/../..//span[@class='price actual-price']"
    _actual_price = driver.find_element_by_xpath(_xpath).text
    if _expected_price == float(_actual_price):
        print('PASS')
    else:
        print('FAIL')
```

### Exercise 5:
**Write a script to add different books to the shopping cart and edit the quantities in the quantity text box**

```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/books")
time.sleep(2)

_books = ['Fiction', 'Science', 'Health Book']
_quantities = [4, 10, 15]
for _book in _books:
    _xpath = "//a[text()='{}']/../..//input[@value='Add to cart']".format(_book)
    driver.find_element_by_xpath(_xpath).click()
    time.sleep(1)

time.sleep(5)

driver.find_element_by_partial_link_text("Shopping cart").click()

for _book, _quantity in zip(_books, _quantities):
    _xpath_quantity = f"(//a[text()='{_book}'])[2]/../..//input[@type='text']"
    driver.find_element_by_xpath(_xpath_quantity).clear()
    driver.find_element_by_xpath(_xpath_quantity).send_keys(_quantity)
    time.sleep(1)

```

### Exercise 6:
**Write a script to select a particular item in the shopping cart and delete the item from cart**

```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/books")
time.sleep(2)

_books = ['Science', 'Health Book', 'Fiction', 'Computing and Internet']

for _book in _books:
    _xpath = "//a[text()='{}']/../..//input[@value='Add to cart']".format(_book)
    driver.find_element_by_xpath(_xpath).click()
    time.sleep(1)

time.sleep(5)

driver.find_element_by_partial_link_text("Shopping cart").click()

_book = "Fiction"
_checkbox = f"(//a[text()='{_book}'])[2]/../..//input[@name='removefromcart']"
driver.find_element_by_xpath(_checkbox).click()

```

### Exercise 7:
**Write a script to print the link text of all the links present in the headers of Yahoo.com**

```python
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')

driver.get("https://in.yahoo.com/?p=us")

sleep(5)

links = driver.find_elements_by_xpath("//ul[@id='header-nav-bar']//a")

for link in links:
    print(link.text)
```
### Exercise 8:
**Write a script to print the table contents in python.org downloads page**

```python
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.python.org/downloads/")
driver.maximize_window()

_xpath_version = "(//ol[@class='list-row-container menu'])[1]//li/span[1]"
_xpath_status = "(//ol[@class='list-row-container menu'])[1]//li/span[2]"
_release_date = "(//ol[@class='list-row-container menu'])[1]//li/span[3]"
_xpath_support = "(//ol[@class='list-row-container menu'])[1]//li/span[4]"
_xpath_schedule = "(//ol[@class='list-row-container menu'])[1]//li/span[5]"

versions = driver.find_elements_by_xpath(_xpath_version)
status = driver.find_elements_by_xpath(_xpath_status)
dates = driver.find_elements_by_xpath(_release_date)
support_status = driver.find_elements_by_xpath(_xpath_support)
schedule = driver.find_elements_by_xpath(_xpath_schedule)

for v, s, d, ss, sch in zip(versions, status, dates, support_status, schedule):
    print(v.text, '\t', s.text, '\t', d.text, '\t', ss.text, '\t', sch.text)
    sleep(1)
```

