### BasePage
* Create a new class “ BasePage”, and keep all the common behaviours, common web elements and anything which is common for all the pages should be developed in the base page class.

* To make all these actions to be available to the page classes, make sure, base page is inheriting to all the page classes.

* By doing this, we can avoid the redundant/duplicate code, reduce the number of lines of code, code quality improves, performance of our project will improve and it will take less memory.


```python
from Data.ExcelLib import read_locators
from Library.SeleniumWrapper import SeleniumWrapper


class BasePage(SeleniumWrapper):
    BasePage_Objects = read_locators("BasePage")

    def __init__(self, driver):
        super().__init__(driver)

    def click_register(self):
        register_locator = BasePage.BasePage_Objects['lnk_register']
        self.click_element(register_locator)

    def click_login_link(self):
        login_locator = BasePage.BasePage_Objects['lnk_login']
        self.click_element(login_locator)

    def enter_search_store(self, search_item):
        search_locator = BasePage.BasePage_Objects['txt_search_store']
        self.enter_text(search_locator, value=search_item)

    def verify_login_success(self):
        locator = BasePage.BasePage_Objects['lnk_logout']
        self.wait_for_element(locator)

    def verify_invalid_email_msg(self):
        locator = BasePage.BasePage_Objects['lbl_invalid_email_msg']
        self.wait_for_element(locator)

    def verify_unregistered_user_msg(self):
        locator = BasePage.BasePage_Objects['lbl_unregistered_user_msg']
        self.wait_for_element(locator)
```

### LoginPage

```python
class LoginPage(BasePage):
    LoginPage_Objects = read_locators("LoginPage")

    def enter_email(self, email):
        locator_email = LoginPage.LoginPage_Objects['txt_email']
        self.enter_text(locator_email, value=email)

    def enter_password(self, password):
        locator_password = LoginPage.LoginPage_Objects['txt_password']
        self.enter_text(locator_password, value=password)

    def click_login_button(self):
        locator_login = LoginPage.LoginPage_Objects['btn_login']
        self.click_element(locator_login)
```

### RegistrationPage
```python
class RegistrationPage(BasePage):
    RegistrationPage_Objects = read_locators("RegistrationPage")

    def select_male(self):
        locator_male = RegistrationPage.RegistrationPage_Objects['rdo_male']
        self.click_element(locator_male)

    def select_female(self):
        locator_female = RegistrationPage.RegistrationPage_Objects['rdo_female']
        self.click_element(locator_female)

    def enter_firstname(self, fname):
        locator_firstname = RegistrationPage.RegistrationPage_Objects['txt_firstname']
        self.enter_text(locator_firstname, value=fname)

    def enter_lastname(self, lname):
        locator_lastname = RegistrationPage.RegistrationPage_Objects['txt_lastname']
        self.enter_text(locator_lastname, value=lname)

    def enter_email(self, email):
        locator_email = RegistrationPage.RegistrationPage_Objects['txt_email']
        self.enter_text(locator_email, value=email)

    def enter_password(self, password):
        locator_password = RegistrationPage.RegistrationPage_Objects['txt_password']
        self.enter_text(locator_password, value=password)

    def enter_confirm_password(self, password):
        locator_confirm_password = RegistrationPage.RegistrationPage_Objects['txt_confirm_password']
        self.enter_text(locator_confirm_password, value=password)

    def click_register_button(self):
        locator_register = RegistrationPage.RegistrationPage_Objects['btn_register']
        self.click_element(locator_register)
```

### Test Script to check for invalid email formats
```python
from Data.ExcelLib import read_data
from POM.BasePage import BasePage
from POM.LoginPage import LoginPage
from parameterized.parameterized import parameterized_class

headers, data = read_data("Login", "test_02")

@parameterized_class(headers, data)
class TestInvalidEmailFormat:
    def test_invalid_email_format(self, set_up):       # Unittest method
        bp = BasePage(set_up)
        bp.click_login_link()
        lp = LoginPage(set_up)
        lp.enter_email(self.Email)
        lp.click_login_button()
        lp.verify_invalid_email_msg()
```
### Test Script to validate error message when tried to login with un-registered user.
```python
from Tests.BaseTest import BaseTest
from Data.ExcelLib import read_data
from POM.BasePage import BasePage
from POM.LoginPage import LoginPage
from parameterized.parameterized import parameterized_class

headers, data = read_data("Login", "test_03")


@parameterized_class(headers, data)
class TestUnregisteredUser(BaseTest):
    def test_unregistered_user(self):       # Unittest method
        bp = BasePage(self.driver)
        bp.click_login_link()
        lp = LoginPage(self.driver)
        lp.enter_email(self.Email)
        lp.click_login_button()
        lp.verify_unregistered_user_msg()
```

### Scenario-1 (Register User)
* Launch demo webshop url.
* Click on register link
* Enter user details in registration page and click on register.
* Verify that the user is registered successfully.

### Scenario-2 (Shopping)
* Launch demo webshop url.
* Login with a registered user.
* Click on Books link.
* Click Add Cart button corresponding to Health Book.
* Click on Shopping Cart(1).
* Accept terms and conditions checkbox and click checkout button.
* Enter Billing Details.
* Enter Shipping Address.
* Select Shipping Method.
* Payment Method.
* Enter Payment Information.
* Click on Confirm Order.

* **BasePageObject**
* ![BasePageObjects](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/BasePage_Objects.png)
* **LoginPageObjects**
* ![LoginPageObjects](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/LoginPage_Objects.png)
* **RegistrationPageObjects**
* ![RegistrationPageObjects](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/RegistrationPage_Objects.png)
* **CartPageObjects**
* ![CartPageObjects](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/CartPage_Objects.png)
* **CheckoutPageObjects**
* ![CheckoutPageObjects](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/CheckoutPage_Objects.png)
* **OrderConfirmationPageObjects**
* ![OrderConfirmationPageObjects](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/OrderConfirmationPage_Objects.png)