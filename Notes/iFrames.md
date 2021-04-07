* An iFrame (Inline Frame) is an HTML document embedded inside the current HTML document on a website.
* Frame or iFrame HTML tag will be used to insert one html page in another html page.
* iFrame HTML element is used to insert content from another source, such as an advertisement, into a Web page.
* iFrame is defined by an <iFrame></iFrame> tag in HTML. With this tag you can identify an iFrame while inspecting the HTML tree.
* In order to embed (include) a web page inside another web page developer uses ‘iFrame’ or ‘Frame’ html tag.
* But, if an element is inside the frame then web driver cannot find the element.
* Webdriver can’t perform an action on web element automatically when object or web element are inside the frame.
* In order to work with frame web elements we should pass driver control to the frame before performing an action.
* There are three ways we can pass driver control to frame.
     * Int 
     * String (ID/Name)
     * Web Element (Address)

* There are three ways we can pass driver control to frame.
```python
driver.switch_to.frame('frame_name')
driver.switch_to.frame(1)
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
```
* In order to give the control back to the main page, i.e. Change the control from frame or to exit from the frame we use the following methods.

```python
driver.switch_to.default_content()
driver.switch_to.parent_frame()
```
* Default content method is used to switch to main page directly.
* Parent frame method is used to switch to its immediate parent page.

**Exercise: 1 Write a script to launch custom HTML page and click on "Business" link present inside a frame (switch to the frame using Index)**
* Index of a Frame is the position at which it occurs in the HTML page. 
* In the sample page we have two Frames, index of Frame starts from 0. So there are two Frames on the page with index 0 and 1
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/iframe.html")

driver.switch_to.frame(0)
driver.find_element_by_xpath("//a[text()='Business']").click()
```

**Exercise: 2 Write a script to launch custom HTML page and click on "Business" link present inside a frame (switch to the frame using Name attribute)**

```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/iframe.html")

driver.switch_to.frame("frame1")
driver.find_element_by_xpath("//a[text()='Business']").click()
```
**Exercise: 3 Write a script to launch custom HTML page and click on "Business" link present inside a frame (switch to the frame using ID attribute)**

```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/iframe.html")

driver.switch_to.frame("FR1")
driver.find_element_by_xpath("//a[text()='Business']").click()
```

**Exercise: 4 Write a script to launch custom HTML page and click on "Business" link present inside a frame (switch to the frame using Webelement object)**

* We can switch to a Frame by simply passing the Frame Web Element to the driver.
* First find the Frame element using any of the locator strategies and then passing it to switch_to command.

```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/iframe.html")

element = driver.find_element_by_xpath("//iframe[@name='frame1']")
driver.swith_to.frame(element)
driver.find_element_by_xpath("//a[text()='Business']").click()
```
**Switching back to Main page from Frame**

* Once you are done with all the task in a particular iFrame you can switch back to the main page using the below statement.
```python
driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/iframe.html")

driver.switch_to.frame(0)
driver.find_element_by_xpath("//a[text()='Business']").click()
driver.switch_to.default_content()
driver.find_element_by_xpath("//a[text()='Google']").click()
```

* Whenever switchTo ().Frame () method fails to locate the frame in a HTML page. We get a NoSuchFrameException.
* Whenever the frame page get refresh, control will automatically go back to the main page.