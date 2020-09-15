from selenium import webdriver
import time


driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/")
time.sleep(2)

# Selecting Checkbox corresponding to different languages
_languages = ['Python', 'Java', 'JavaScript']
for _language in _languages:
    _xpath = f"//td[text()='{_language}']/..//input[@name='download']"
    driver.find_element_by_xpath(_xpath).click()
    time.sleep(1)

_votes = ['Good', 'Excellent', 'Poor']
for _vote in _votes:
    _xpath = f"//label[text()='{_vote}']/..//input[@type='radio']"
    driver.find_element_by_xpath(_xpath).click()
    time.sleep(1)

_releases = ['Python 3.7.8', 'Python 3.8.3', 'Python 2.7.17']
for _release in _releases:
    _xpath = f"//a[text()='{_release}']/../..//a[text()=' Download']"
    print(driver.find_element_by_xpath(_xpath).text)
    time.sleep(1)


_release_notes = "//a[text()='Python 3.7.8']/../..//a[text()='Release Notes']"

_items = ['$25 Virtual Gift Card',
          '14.1-inch Laptop',
          'Build your own cheap computer',
          'Simple Computer',
          'Build your own expensive computer',
          'Build your own computer']

_expected_prices = [25.00, 2000.00, 800.00, 800.00, 1800.00, 1200.00]

price_tag = {
             "$25 Virtual Gift Card": 25.00,
             '14.1-inch Laptop': 2000.00,
             'Build your own cheap computer': 800.00,
             'Simple Computer': 800.00,
             'Build your own expensive computer': 1800.00,
             'Build your own computer': 1200.00
             }

for _item, _expected_price in price_tag.items():
    print(f'Validating Price of {_item} ', end='')
    _xpath = f"//a[text()='{_item}']/../..//span[@class='price actual-price']"
    _actual_price = driver.find_element_by_xpath(_xpath).text
    if _expected_price == float(_actual_price):
        print('PASS')
    else:
        print('FAIL')

for _item, _expected_price in zip(_items, _expected_prices):
    print(f'Validating Price of {_item} ', end='')
    _xpath = f"//a[text()='{_item}']/../..//span[@class='price actual-price']"
    _actual_price = driver.find_element_by_xpath(_xpath).text
    if _expected_price == float(_actual_price):
        print('PASS')
    else:
        print('FAIL')

