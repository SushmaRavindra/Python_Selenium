from selenium import webdriver
import time


driver = webdriver.Chrome('./chromedriver')
driver.get("http://demowebshop.tricentis.com/books")
time.sleep(2)

# Selecting Checkbox corresponding to different languages
_languages = ['Python', 'Java', 'JavaScript']
for _language in _languages:
    _xpath = f"//td[text()='{_language}']/..//input[@name='download']"
    driver.find_element_by_xpath(_xpath).click()
    time.sleep(1)

# Selecting Different Voting radio buttons
_votes = ['Good', 'Excellent', 'Poor']
for _vote in _votes:
    _xpath = f"//label[text()='{_vote}']/..//input[@type='radio']"
    driver.find_element_by_xpath(_xpath).click()
    time.sleep(1)

# Printing text of download link of different python  releases
_releases = ['Python 3.7.8', 'Python 3.8.3', 'Python 2.7.17']
for _release in _releases:
    _xpath = f"//a[text()='{_release}']/../..//a[text()=' Download']"
    print(driver.find_element_by_xpath(_xpath).text)
    time.sleep(1)

# Getting Price tag of different items in demo shopping cart (Using List's)
_items = ['$25 Virtual Gift Card',
          '14.1-inch Laptop',
          'Build your own cheap computer',
          'Simple Computer',
          'Build your own expensive computer',
          'Build your own computer']

_expected_prices = [25.00, 1590.00, 800.00, 800.00, 1800.00, 1200.00]

for _item, _expected_price in zip(_items, _expected_prices):
    print(f'Validating Price of {_item}: ', end='')
    _xpath = f"//a[text()='{_item}']/../..//span[@class='price actual-price']"
    _actual_price = driver.find_element_by_xpath(_xpath).text
    if _expected_price == float(_actual_price):
        print('PASS')
    else:
        print('FAIL')

# Using Dictionary
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

quantities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for quantity in quantities:
    driver.find_element_by_xpath("(//a[text()='Science'])[2]/../..//input[@type='text']").clear()
    driver.find_element_by_xpath("(//a[text()='Science'])[2]/../..//input[@type='text']").send_keys(quantity)
    time.sleep(0.5)

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
