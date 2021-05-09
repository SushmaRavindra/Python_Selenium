### find_elements
* It returns list of web elements.
* If the locator is matching with one element, find_elements function returns list of web elements with size 1.
* If the locator is not matching with any of the web elements, then the function returns an empty list.

### Exercise :1
**Checking all the checkboxes on the webpage.**
```python
from selenium import webdriver
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///HTML_Pages/Tables.html')

time.sleep(2)

elements = driver.find_elements_by_name("download")

for element in elements:
    element.click()
    time.sleep(1)

time.sleep(2)
driver.quit()
```
### Exercise :2
**Checking all the checkboxes in reverse order**
```python
from selenium import webdriver
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///HTML_Pages/Tables.html')

time.sleep(2)

elements = driver.find_elements_by_name("download")

for element in reversed(elements):
    element.click()
    time.sleep(1)

time.sleep(2)
driver.quit()
```
**Alternate Solution (Using slicing syntax)**
```python
for element in elements[::-1]:
    element.click()
    time.sleep(1)
```

### Exercise :3
**Checking alternate checkboxes**
```python
from selenium import webdriver
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///HTML_Pages/Tables.html')

time.sleep(2)

elements = driver.find_elements_by_name("download")

for element in elements[::2]:
    element.click()

time.sleep(2)
driver.quit()
```
### Exercise :4
**Checking only first and last checkbox**
```python
from selenium import webdriver
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///HTML_Pages/Tables.html')

time.sleep(2)

elements = driver.find_elements_by_name("download")

elements[0].click()
time.sleep(1)
elements[-1].click()

time.sleep(2)
driver.quit()
```
### Exercise :5
**Printing total number of links on the custom webpage and link text of all the links.**
```python
from selenium import webdriver
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('file:///HTML_Pages/Tables.html')

time.sleep(2)

links = driver.find_elements_by_xpath("//a")

print('Total link on the page: ',len(links))

for link in links:
    print(link.text)

time.sleep(2)
driver.quit()
```

### Exercise :6
**Count number of images on the webpage**
```python
from selenium import webdriver
import time

# Instantiate a Chrome Browser
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get('http://demowebshop.tricentis.com/')

time.sleep(2)

images = driver.find_elements_by_xpath("//img")

print('Total Images on the page: ',len(images))

time.sleep(2)
driver.quit()
```
### Exercise :7
**Print the link text of all the links in python.org iff the linktext contains word 'Python' in it. Also, print the attribute 'href' of the corresponding link.**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org/")
time.sleep(3)
links = driver.find_elements_by_xpath("//a")

for link in links:
    if 'Python' in link.text:
        print(link.text, end=',')
        print(link.get_attribute("href"))
```
**Alternate Solution**
* Use find_elements_by_tag_name
* Use find_elements_by_partial_link_text
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org/")
time.sleep(3)
links = driver.find_elements_by_partial_link_text("Python")

for link in links:
    print(link.text, end=',')
    print(link.get_attribute("href"))
```
### Exercise :8
**Print the link text of all the links in spiders.com iff the linktext contains word 'spiders' in it. Also, print the attribute 'href' of the corresponding link.**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.qspiders.com/")
time.sleep(3)
links = driver.find_elements_by_xpath("//a")

for link in links:
    if 'spiders' in link.text:
        print(link.text, end=',')
        print(link.get_attribute("href"))
```
**Alternate Solution**
* Use find_elements_by_partial_link_text
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.qspiders.com/")
time.sleep(3)

links = driver.find_elements_by_partial_link_text("Spiders")

for link in links:
    print(link.text)
```
### Exercise :9
**Print the title of all the images in demowebsop iff the title contains word 'computer' in it.**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/")
time.sleep(3)

images = driver.find_elements_by_tag_name('img')

for image in images:
    _title = image.get_attribute("title")
    if 'computer' in _title:
        print(_title)
```
### Exercise: 10
**Write a script to print the link text and href attribute of all the links present on the header of yahoo.com**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.yahoo.com")

links = driver.find_elements_by_xpath("//ul[@id='header-nav-bar']//a")
for link in links:
  text = link.text
  url = link.get_attribute("href")
  print(f'{text:<20} {url:<40}')
```
### Exercise :11
**Write a script enter firstname and lastname in custom webpage (sample.html) using for loop.**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.yahoo.com")

elements = driver.find_elements_by_name("spam")
texts = ['Hello', 'World']

for element, text in zip(elements, texts):
    element.send_keys(text)
    time.sleep(1)
```

