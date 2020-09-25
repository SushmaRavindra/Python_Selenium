# from selenium import webdriver
#
# driver = webdriver.Chrome('./chromedriver')
# driver.get("http://demowebshop.tricentis.com/")
#
#
# def click_element(loctype, locvalue):
#     driver.find_element(loctype, locvalue).click()
#
#
# def enter_text(loctype, locvalue, value):
#     driver.find_element(loctype, locvalue).send_keys(value)
#
#
# click_element("xpath", "//a[text()='Register']")
# enter_text("name", "FirstName", "Hello")
# click_element("id", "gender-male")
# click_element("name", "register-button")


def even_numbers(number):
    return number % 2 == 0

def palindrome(s1, s2):
    return s1 == s2[::-1]

import unittest
class Test(unittest.TestCase):
    def test_even(self):
        self.assertTrue(even_numbers(10))

    def test_odd(self):
        self.assertFalse(even_numbers(9))