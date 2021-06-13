## Client Libraries / Language Bindings.
* Selenium supports multiple languages such as Python, Java, C#, Javascript, Ruby.
* Client libraries provide various methods to perform different browser actions. e.g. get, title, current_url find_element etc.
* As automation developers we call these methods from our development environment. e.g. PyCharm IDE.
* Once we execute the script, the client libraries convert our code that we have written into a JSON (javascript Object Notation) format and sent as a request to Driver over HTTP.

## Browser Drivers.
* Each browser has its own implementation of "WebDriver" protocol (mandatory services that need's to be implemented in order for selenium to interact with browser) called drivers.
* The browser drivers are responsible for controlling the actual browser's since the browser implementation details will be known only to the developer of driver.
* Each browser driver will be maintained by respective browser vendor. e.g Chrome Driver is maintained by Google and Safari Driver is maintained by Apple.
* Each method in the client library is mapped to a specific web-service in the driver.
* The driver interprets the incoming request from the client and controls the actual browser.
* Once the browser operation is complete, the response is sent back to the client/client library by driver in JSON format.
* Client library interprets the JSON response and prints the response in readable format in the Pycharm console.

## Browsers
Selenium officially supports Edge, IE, Chrome, Firefox, Safari, Opera.

## Architecture Diagram

![Architecture Diagram](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/Selenium_Architecture.png)

## Useful links
* [Official Python-Selenium documentation](https://www.selenium.dev/selenium/docs/api/py/index.html)
* [Download Chrome Driver](https://chromedriver.chromium.org/downloads)
* [Download Gecko Driver](https://github.com/mozilla/geckodriver/releases)
* [Download Internet Explorer Driver](https://selenium-release.storage.googleapis.com/index.html)
* [Download Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Vendor driver documentation (As per WebDriver Protocol)
* [Chrome WebServices](https://chromium.googlesource.com/chromium/src/+/master/docs/chromedriver_status.md)
* [Safari WebServices](https://developer.apple.com/documentation/webkit/macos_webdriver_commands_for_safari_11_1_and_earlier)
* [Microsoft Edge WebServices](https://docs.microsoft.com/en-us/microsoft-edge/edgehtml/webdriver/)

```python
# Launch Chrome
r1 = request('POST', 'http://127.0.0.1:9515/session', json={"capabilities": {"browsername": "chrome"}})
resp = json.loads(r1.text)
session_id = resp['value']['sessionId']

# Navigate to a URL
r2 = request("POST", f'http://127.0.0.1:9515/session/{session_id}/url', json={"url": "http://demowebshop.tricentis.com/"})

# Get Element (Register)
r3 = request("POST", f'http://127.0.0.1:9515/session/{session_id}/element', json={"using": "link text", "value": "Register"})
resp = json.loads(r3.text)
element_id = resp['value']['element-6066-11e4-a52e-4f735466cecf']

# Click on Register
r4 = request("POST", f'http://127.0.0.1:9515/session/{session_id}/element/{element_id}/click', json={})

# Get Element (Male Radio Button)
r5 = request("POST", f'http://127.0.0.1:9515/session/{session_id}/element', json={"using": "xpath", "value": "//input[@id='gender-male']"})
resp = json.loads(r5.text)
element_id = resp['value']['element-6066-11e4-a52e-4f735466cecf']

# Click on Male Radio Button
r6 = request("POST", f'http://127.0.0.1:9515/session/{session_id}/element/{element_id}/click', json={})

# Get Element (Firstname)
r7 = request("POST", f'http://127.0.0.1:9515/session/{session_id}/element', json={"using": "xpath", "value": "//input[@name='FirstName']"})
resp = json.loads(r7.text)
element_id = resp['value']['element-6066-11e4-a52e-4f735466cecf']

# Enter Firstname
r8 = request("POST", f'http://127.0.0.1:9515/session/{session_id}/element/{element_id}/value',json = {"text": "Sandeep", "value": "Sandeep"})

# Get Element (Lastname)
r9 = request("POST", f'http://127.0.0.1:9515/session/{session_id}/element', json={"using": "xpath", "value": "//input[@name='LastName']"})
resp = json.loads(r9.text)
element_id = resp['value']['element-6066-11e4-a52e-4f735466cecf']

# Enter LastName
r10 = request("POST", f'http://127.0.0.1:9515/session/{session_id}/element/{element_id}/value',json = {"text": "Suryaprasad", "value": "Suryaprasad"})
```




