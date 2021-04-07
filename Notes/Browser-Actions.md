**Instantiate a Chrome Browser**
```python
from selenium import webdriver
driver = webdriver.Chrome("/users/demo/training/chromedriver")
```
**Instantiate a Safari Browser**
```python
from selenium import webdriver
driver = webdriver.Safari()  # Driver path will be automatically taken from /usr/bin
                              # To enable safari driver run the command /usr/bin safaridriver --enable
```
**Instantiate a Firefox Browser**
```python
from selenium import webdriver
driver = webdriver.Firefox("/users/demo/training/geckodriver")
```
**Instantiate a IE Browser**
```python
from selenium import webdriver
driver = webdriver.Ie("/users/demo/training/iedriver")
```
**Maximize Browser**
```python
from selenium import webdriver
driver.maximize_window()
```

**Launch URL**

```python
from selenium import webdriver
driver.get('http://www.google.com')
```
**Get Current URL**
```python
from selenium import webdriver
curr_url = driver.current_url
```

```python
# Launch google.com and verify if the current URL is "http://google.com"
from selenium import webdriver
driver.get('http://www.google.com')

_actual_url = driver.current_url

_expected_url = "https://www.google.com"

_actual_url = _actual_url[:22]

if _actual_url == _expected_url:
    print('PASS')
else:
    print('FAIL')
```
**Get Page Title**
```python
_title = driver.title
# Launch google.com and verify if the Page title is "Google'
from selenium import webdriver
driver.get('http://www.google.com')

_actual_title = driver.title

_expected_title = "Google"

if _actual_title == _expected_title:
    print('PASS')
else:
    print('FAIL')
```

**Refreshing the Broswer**
```python
driver.refresh()
```
**Browser Back**
```python
driver.back()
```

**Browser Forward**
```python
driver.forward()
```
**Closing Browser**

```python
driver.close()   # Closes only parent browser or window

driver.quit()    # Closes parent as well as child browser's or window's

```