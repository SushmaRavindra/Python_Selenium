**ActionChains**

ActionChains class is used for:
* Handling Dropdown menu.
* Sending/Simulating keyboard inputs.
* Context Click.
* Double Click.
* Drag and Drop.

### Exercise 1:
**Write a script to open custom HTML page and mouse hover on "About", "Blog", "Projects", "Contact" menu's****
```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Mouse_Hover.html#")
time.sleep(2)
menus = ['About', 'Blog', 'Projects', 'Contact']
actions = ActionChains(driver)
for menu in menus:
    _menu_xpath = f"//a[text()='{menu}']"
    element = driver.find_element_by_xpath(_menu_xpath)
    actions.move_to_element(element).perform()
    time.sleep(1)
```
### Exercise 2:
**Write a script to open custom HTML page and mouse hover on "About"-->"Careers" (Multiple Menus)**

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Multiple_Menue.html#home")
time.sleep(3)

actions = ActionChains(driver)
about = driver.find_element_by_xpath("//button[text()='About ']")
careers = driver.find_element_by_xpath("//a[text()='Careers']")
actions.move_to_element(about).perform()
time.sleep(1)
actions.move_to_element(careers).perform()
```
### Exercise 3:
**Write a script to mouse Hover on "MEN" and click on T-Shirts in myntra.com**
```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver.get('https://www.myntra.com/')
sleep(5)
kids = driver.find_element_by_xpath("//a[text()='Men']")
a = ActionChains(driver)
a.move_to_element(kids).perform()
sleep(5)
driver.find_element_by_xpath("(//a[text()='T-Shirts'])[1]").click()
```
### Exercise 4:
**Write a script to launch monster.com, mouse hover on Jobs Search-->Jobs By Skills and click on Python Jobs**
```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.monsterindia.com/")
sleep(5)

actions = ActionChains(driver)
job_search = driver.find_element_by_xpath("//a[text()='Job search']")

# Mouse Hover on Job Search link
actions.move_to_element(job_search).perform()

jobs_by_skills = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")

# Mouse Hover on Jobs By Skills link
actions.move_to_element(jobs_by_skills).perform()

# Click on Python Jobs link
driver.find_element_by_xpath("//a[contains(text(),'Python Jobs')]").click()
```

### Exercise 5:
**Simulating/Sending keyboard inputs to the focussed element on the webpage**

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()
actions.send_keys(Keys.PAGE_DOWN).perform()
actions.send_keys(Keys.PAGE_UP).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ESCAPE).perform()
actions.send_keys(Keys.SHIFT).perform()
actions.send_keys(Keys.CONTROL)
```
### Exercise 6:
**Write a script to double click on a custom HTML webpage**
```python
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Double_Click.html")
time.sleep(3)

actions = ActionChains(driver)
element = driver.find_element_by_xpath("//button[text()='Double-click me']")
actions.double_click(element).perform()
```