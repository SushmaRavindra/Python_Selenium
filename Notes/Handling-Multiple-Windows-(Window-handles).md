### Pop ups are categorized into following types

* Child-browser pop up or HTML pop up
* Alert/Confirmation/Java Script pop up
* Notification pop up
* File upload pop up
* File download pop up
* Window pop up
* Calendar pop up

### Child-browser pop up or HTML pop up
Child browser pop-up are small pop-up over the top of the web pages in the internet browser. e.g. new tabs, new windows.

**Characters**
* We can inspect it.
* We can move it.
* It contains minimise, maximise and close buttons.
* It may contain address bar.

* In order to handle the child browser, first we have to transfer the driver control from main browser window to the child browser.
* For every browser opened by selenium, it generates a unique alpha numeric string called window handle.

### Exercise: 1
**Write a script to close all the browsers in naukri.com without using quit() method.**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.naukri.com/")
time.sleep(4)

win_handles = driver.window_handles  # Get all the window handles
for handle in win_handles:
    driver.switch_to.window(handle)
    driver.close()
```
### Exercise: 2
**Write a script to count the number of browsers opened by selenium**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.naukri.com/")
time.sleep(4)

win_handles = driver.window_handles  # Get all the window handles
print('No of Browsers: ',len(win_handles))
```

### Exercise: 3
**Write a script to close all the browsers in reversed order**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.naukri.com/")
time.sleep(4)

win_handles = driver.window_handles  # Get all the window handles

for handle in reversed(win_handles):
    driver.switch_to.window(handle)
    driver.close()
```
**Alternate Solution**
Using Slicing Syntax
```python
for handle in win_handles[::-1]:
    driver.switch_to.window(handle)
    driver.close()
```
### Exercise: 4
**Write a script to open demowebshop site, click on Facebook link present at the bottom of the webpage. Close Facebook browser window opened in new tab**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/")
time.sleep(4)

driver.find_element_by_xpath("//a[text()='Facebook']").click()

win_handles = driver.window_handles
driver.switch_to.window(win_handles[1])  # Switch to Facebook tab on the browser
driver.close()
```
### Exercise: 5
**Write a script to print the title of all the browsers in naukri.com**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
win_handles = driver.window_handles  # Get all the window handles

for handle in win_handles:
    driver.switch_to.window(handle)
    print(driver.title)
```
### Exercise: 6
**Write a script to open naukri.com, close the browser which has the title "Amazon"**
```python
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
win_handles = driver.window_handles  # Get all the window handles

for handle in win_handles:
    driver.switch_to.window(handle)
    if driver.title == 'Amazon':
       driver.close()
```
### Exercise: 7
**Write a script to close all browsers except parent browser**
```python
from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.naukri.com/")
time.sleep(4)

win_handles = driver.window_handles
for index, win in enumerate(win_handles):
    if index == 0:
        continue
    driver.switch_to.window(win_handles[index])
    driver.close()
    time.sleep(1)
```
### Alert/Confirmation/Java Script pop up

Alert is a small message box which displays on-screen notification to give the user some kind of information or ask for permission to perform certain kind of operation. It may be also used for warning purpose.

**Characteristics of alert pop up**
* We cannot inspect the pop-up
* We can move the pop-up
* It contains minimise, maximise and close buttons.
* It contains only one button (‘YES’ or ‘NO’) or two buttons (‘Cancel’ and ‘OK’).
* This kind of pop-up is also called as web based pop-up and java script pop-up.
* In order to perform operation on the alert pop-up, we first transfer the control from webpage
 to the pop-up.
* Selenium provides us with a class called Alert.

### Exercise: 7
**Write a script to open custom webpage, click on Try it button and click on OK Button**
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Javascript_Alert.html")

driver.switch_to.alert.accept()
```
### Exercise: 8
**Write a script to open custom webpage, click on Try it button and click on Cancel Button**
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Javascript_Alert.html")

driver.switch_to.alert.dismiss()
```
### Exercise: 9
**Write a script to open custom webpage, click on Try it button and get the text of the alert**
```python
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Javascript_Alert.html")

print(driver.switch_to.alert.text)
```
**Note: If the alert popup is not present, NoAlertPresentException is raised by webdriver** 

### Notification Popup
* Push Notifications are mainly used to deliver information instantly on the user's browser like Latest news alert, New blog post, Sale event, Flight notifications, Score update for sports. E-commerce websites have been the early adopter of this tool. 

* Slowly, other industries like travel, blog, media, and medical sites have started using push notification for its ease of use and effectivenes

* Web Notification: It works only when a user is on the website. The user will receive the notification only if present on the website.

* Web Push Notifications: It works even when the user is not on your site. It is delivered in real-time on the browser and doesn’t depend on which site user is browsing.

![Pushnotification2](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/PushNotification2.png)
![Pushnotification](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/PushNotification.png)
![Pushnotification3](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/PushNotification3.png)
![Pushnotification4](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/Push_Notification4.png)
![Pushnotification5](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/Push_Notification5.png)

**Characteristics of Push Notification Popup**

* We cannot Inspect.
* We cannot Move the Popup

In order to handle this popup, options/profile (Chrome/Firefox) class used.

**Chrome Browser**
```python
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--disable-notifications")
driver = webdriver.Chrome('./chromedriver', options=chromeOptions)
driver.get("https://www.redbus.in/")
```

**Firefox Browser**
```python
from selenium import webdriver

firefoxProfile = webdriver.FirefoxProfile()
firefoxProfile.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(options=firefoxProfile)
driver.get("https://www.redbus.in/")
```
### Myntra.com
```python
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
opts = webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")
driver = webdriver.Chrome('./chromedriver', options=opts)
driver.get('https://www.myntra.com/')

sleep(5)
kids = driver.find_element_by_xpath("//a[text()='Men']")
a = ActionChains(driver)
a.move_to_element(kids).perform()
sleep(5)
driver.find_element_by_xpath("(//a[text()='T-Shirts'])[1]").click()
```
### File Download popup
* File download popup can be handled either by using 3rd party library called PyAutoIT or programatically (through ChromeOptions and FireFoxProfile class).

**Program to download Desktop version of watsapp in chrome browser.**
```python
from selenium import webdriver
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("prefs",{"download.default_directory": r"/users/sandeep/documents",
                                    "safebrowsing.enabled": True}
                             )
driver = webdriver.Chrome('./chromedriver', options=opts)
driver.get("https://www.whatsapp.com/download/")
sleep(5)
driver.find_element_by_xpath("//a[text()='Download for Mac OS X']").click()
```

**Program to download Desktop version of watsapp in Firefox browser.**
```python
from selenium import webdriver
from time import sleep

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", '/users/sandeep/documents')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
driver = webdriver.Firefox(profile)
driver.get("https://www.whatsapp.com/download/")
sleep(5)
driver.find_element_by_xpath("//a[text()='Download for Mac OS X']").click()
```
