### Locators in Selenium
Selenium uses 8 different locators to identify object on the webpage.
1. name
2. id
3. Linktext
4. Partial Linktext
5. Tagname
6. Class
7. CSS Selector
8. xPath

### find_element
* find_element method returns a web element if the element is found in the DOM/HTML.
* If no element is found, find_element method throws "NoSuchElementException".
* If there are multiple elements matching the same locator, find_element method returns the first matching element from the DOM.

**Identifying the elements using "name", "id" and "linkText"**
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
time.sleep(3)

driver.find_element_by_link_text("Register").click()

time.sleep(2)

driver.find_element_by_name("FirstName").send_keys("Steve")

time.sleep(2)

driver.find_element_by_id("LastName").send_keys("Jobs")

time.sleep(2)

driver.find_element_by_id("register-button").click()
```
**find_element_by_partial_link_text**
* Finds an element by a partial match of its link text

**Code to click on Shopping Cart link on the demowebshop page using partial linktext.**
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
time.sleep(3)

# Click on ShoppingCart link.
driver.find_element_by_partial_link_text("Shopping").click()
```
**Click on Inbox link irrespective of number of emails.**
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("file:///Users/HTML_Pages/_partial.html")
time.sleep(3)

driver.find_element_by_partial_link_text("Inbox").click()
```
**find_element_by_class_name**

**Enter username filed in actitime login page using class name**
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('https://demo.actitime.com/login.do')
driver.find_element_by_class_name('textField').send_keys("admin")
```
**Click on Register Link on Home page of Demowebshop using class name**
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('http://demowebshop.tricentis.com/')
driver.find_element_by_class_name('ico-register').click()
```
If the class name has spaces, then it is considered as two different classes in CSS file. So for selenium to identify element by class name with spaces, the space should be replaced by dot operator "."

**Enter Username and Password in actitime login page using class name**
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('https://demo.actitime.com/login.do')
driver.find_element_by_class_name('textField').send_keys("admin")
driver.find_element_by_class_name('textField.pwdfield').send_keys("manager")
```

**Enter Search item and click on Search button on Homepage of demowebshop using class name**
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('http://demowebshop.tricentis.com/')
driver.find_element_by_class_name('search-box-text.ui-autocomplete-input').send_keys('Computer')
driver.find_element_by_class_name('button-1.search-box-button').click()
```

**Enter Search item and click on Search button on Homepage of smartbear webpage**
```python
from selenium import webdriver

driver = webdriver.Chrome('./selenium_training/chromedriver')
driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/")
driver.find_element_by_class_name("instasearch-term.form-control").send_keys("Computer")
driver.find_element_by_class_name("btn.btn-primary.btn-icon.instasearch-button").click()

```

**find_element_by_css_selector**

```
Example:
<html>
  <body>
     Username<input type="text"></input>
     Password<input type="password"></input>
  </body>
</html>
```
* In the above HTML webpage, to identify username and password field, we can not use "name", "id", "linktext" and "partialLinkText" to identify the element as there are no such attributes attached to the input fields. In such scenario we can use the cssSelector (Cascaded Style Sheet) with the following syntax:

**General Format for cssSelector.**
* HTMLTAG[property="value"]

* e.g. input[type="text"] # cssSelector expression for Username
* e.g. input[type="password"] # cssSelector expression for Password

**Selenium code to enter "Computer" and click on "Search" button in demowebshop site using cssSelector.**

```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
time.sleep(3)

driver.find_element_by_css_selector("input[value='Search store']").send_keys("Computer")
time.sleep(3)
driver.find_element_by_css_selector("input[value='Search']").click()
```

**Selenium code to click on "Register" link in demowebshop site using cssSelector.**
```python
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/")
sleep(5)

driver.find_element_by_css_selector("a[class='ico-register']").click()
```
### Xpath

```
<html>
  <body>
      FirstName<input type="text"></input>
      LastName<input type="text"></input>
  </body>
</html>
```
* In the above HTML code, both firstname and last name has same properties. Hence we cannot use cssSelector expression to enter firstname and last name. In such cases we need to go for Xpath.

* Xpath is the path of the element in HTML tree.
* While writing the xpath expression we specify the path using "/" (forward slash)
* First forward slash "/" represent the beginning of the HTML tree, it is called as root.
* After every "/" we must specify HTML tag for the immediate child node.
* If there are any duplicate elements, then we use index. It should be used in square brackets "[]". Index starts from Digit one.

**Consider sample HTML code below**
```
<html>
	<body>
	<div>
		Firstname<input></input>
		Lastname<input></input>
	</div>
	<div>
		Company<input></input>
		Location<input></input>
	</div>
	<body>
</html>
```
**Below is the HTML Hierarchy**

```
html
  body
    div ------> Division-1
      input  ----> Input-1
      input   -----> Input-2
    div ------> Division-2
      input ----> Input-1
      input  ----> Input-2
```
**Absolute xpath**
* Specifying the complete path of the element is called absolute xpath.

**Absolute xpath's**  
```
/html/body/div[1]/input[1]    Matches Firstname
/html/body/div[1]/input[2]    Matches Lastname 
/html/body/div[2]/input[1]    Matches Company
/html/body/div[2]/input[2]    Matches Location
/html/body/div/input          Matches all inputs
/html/body/div[1]/input       Matches Firstname and Lastname
/html/body/div[2]/input       Matches Company and Location
/html/body/div/input[1]       Matches Firstname and Company
/html/body/div/input[2]       Matches Lastname and Location
```

* Since Absolute xpath is very lengthy and it is not practically possible to write relative xpath for bigger web applications with complex HTML hierarchy. 
* To overcome the above problem, we use Relative xpath.

* "/" (Single forward slash) represents immediate child
* "//" (Double forward slash) represents any child.

**Relative xpath's** 
```
//input          Matches all text box's
(//input)[1]     Matches Firstname
(//input)[2]     Matches Lastname
(//input)[3]     Matches Company
(//input)[4]     Matches Location  
//div[1]//input  Matches Firstname and Lastname
//div[2]//input  Matches Company and Location
//div//input[1]  Matches Firstname and Company
//div//input[2]  Matches Lastname and Location
```
### General format of the xpath
* HTMLTAG[@Property="Value"]
* If the "text" attribute is used in the xpath, 
* HTMLTAG[text()='value']
* HTMLTAG[contains(@property, "value")]        # To Ignore white spaces
* HTMLTAG[contains(text(), "value")] 

**Code to enter "Computer" in search box of demowebshop website and click on search button.**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
time.sleep(3)

driver.find_element_by_xpath("//input[@class='search-box-text ui-autocomplete-input']").send_keys("Computer")
driver.find_element_by_xpath("//input[@type='submit']").click()
```

**Code to enter Firstname, Surname and clicking on Signup button on Facebook.com.**

```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
time.sleep(3)

driver.find_element_by_xpath("//input[@name='firstname']").send_keys("Hello")
driver.find_element_by_xpath("//input[@name='lastname']").send_keys("World")
driver.find_element_by_xpath("//button[@name='websubmit']").click()
```
**Code to click on register link on demowebshop page, enter firstname and lastname and click on Register button**

```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
time.sleep(3)

driver.find_element_by_xpath("//a[text()='Register']").click()

time.sleep(2)

driver.find_element_by_xpath("//input[@value='M']").click()

time.sleep(2)

driver.find_element_by_xpath("//input[@id='FirstName']").send_keys("Steve")

time.sleep(2)

driver.find_element_by_xpath("//input[@name='LastName']").send_keys("Jobs")

time.sleep(2)

driver.find_element_by_xpath("//input[@value='Register']").click()
```
**Code to click on a radio button and click on "Vote" button on demowebshop**

```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
time.sleep(3)

driver.find_element_by_xpath("//input[@value='2']").click()

time.sleep(2)

driver.find_element_by_xpath("//input[@value='Vote']").click()
```
