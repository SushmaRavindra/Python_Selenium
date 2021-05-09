### WebDriver Wait (Explicit wait)

**visibility_of**
* visibility_of checks if the web element is visible on the webpage. If the element is not visible within timeout period, then "TimeoutException" is raised.
* If the element is not present on the DOM, then "NoSuchElementException" is raised.
* So to use the above condition, make sure that the element is present on the DOM.

```python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome('chromedriver')
driver.get("file:///Users/HTML_Pages/loading.html")

wait = WebDriverWait(driver, timeout=10)
wait.until(ec.visibility_of(driver.find_element_by_name("fname")))
driver.find_element_by_name("fname").send_keys("Steve")
driver.find_element_by_name("lname").send_keys("Jobs")
```
**visibility_of_element_located**
* visibility_of_element_located checks if the web element is present on the DOM and also visible on the webpage. (Both conditions will be checked)
* "TimeoutException" will be raised if either the element is not loaded onto the DOM or the element is not visible on the web page within timeout period.
* The above condition makes sure that the element is present on DOM and also visible on the web page.
* If the element is visible and is disabled due to some reasons, then "ElementNotInteractableException" is raised.

**Example-1**
```python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome('chromedriver')
driver.get("file:///Users/HTML_Pages/_loading.html")
wait = WebDriverWait(driver, timeout=6)

wait.until(ec.visibility_of_element_located(("name", "fname")))
driver.find_element_by_name("fname").send_keys("Steve")
driver.find_element_by_name("lname").send_keys("Jobs")
```

**Example-2**
```python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome('chromedriver')
driver.get("file:///Users/HTML_Pages/progressbar.html")
wait = WebDriverWait(driver, timeout=10)

wait.until(ec.visibility_of_element_located(("xpath", "//div[text()='100%']")))

```
**invisibility_of_element**
* invisibility_of_element takes web element as an argument. It throws "TimeoutException" if the element is visible even after the timeout period.
* If the web element does not exist on the DOM, "NoSuchElementException" is raised.

**invisibility_of_element_located**
* invisibility_of_element_located takes by locator as an argument. It throws "TimeoutException" if the element is visible even after the timeout period that is specified.
* If the web element does not exist on the DOM, "NoSuchElementException" or "StaleElementReferenceException" is NOT RAISED.

**element_to_be_clickable**
* element_to_be_clickable takes by locator as an argument. It throws "ElementNotClickableException" if the element to be clicked is either not visible or not enabled or missing from the DOM.

**alert_is_present**
* alert_is_present raises "TimeoutException" if the JavaScript Alert is not displayed with in the timeout period.


### Simple One
```python
# Custom class to check for visible and enabled!
class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        is_visible = super().__call__(driver)    # Calling Parent class __call__ method
        enabled = driver.find_element(*self.locator).is_enabled()
        return is_visible and enabled
```
```python
def wait(func):
    def wrapper(*args, **kwargs):
        instance, locator = args
        w = WebDriverWait(instance.driver, 10)
        w.until(_visibility_of_element_located(locator))
        return func(*args, **kwargs)
    return wrapper
```
### Parameterised Decorator for wait
```python
def wait(*, visible=True, enabled=True, alert=False, timeout=10):
    def _func(func):
        def wrapper(*args, **kwargs):
            if alert:
                instance, = args
                w = WebDriverWait(instance.driver, timeout)
                w.until(alert_is_present(), message='Alert Was not Visible')
            elif visible and enabled:
                instance, locator = args
                w = WebDriverWait(instance.driver, timeout)
                w.until(_visibility_of_element_located(locator), message="Element was either not visible or enabled")
            elif visible and not enabled:
                instance, locator = args
                w = WebDriverWait(instance.driver, timeout)
                w.until(visibility_of_element_located(locator), message="Element was not visible")
            elif not visible:
                instance, locator = args
                w = WebDriverWait(instance.driver, timeout)
                w.until(invisibility_of_element_located(locator), message='Element was not invisible within timeout period')
            return func(*args, **kwargs)   # func(self, ("name", 'fname'), value="Hello")
        return wrapper
    return _func
```
