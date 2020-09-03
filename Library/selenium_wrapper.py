from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from Library.config import Config


class Wrapper:
    def __init__(self):
        self.driver = None

    def launch_url(self):
        browser = Config.BROWSER_TYPE
        if browser.upper() == "CHROME":
            self.driver = webdriver.Chrome(Config.CHROME_DRIVER)
        elif browser.upper() == 'FIREFOX':
            self.driver = webdriver.Firefox(Config.GECKO_DRIVER)
        elif browser.upper() == 'SAFARI':
            self.driver = webdriver.Safari()
        self.driver.get(Config.URL)
        time.sleep(3)

    def enter_text(self, locator, value):
        loctype, locvalue = locator
        self.driver.find_element(loctype, locvalue).clear()
        self.driver.find_element(loctype, locvalue).send_keys(value)

    def click_element(self, locator):
        loctype, locvalue = locator
        self.driver.find_element(loctype, locvalue).click()

    def select_item(self, locator, item):
        loctype, locvalue = locator
        element = self.driver.find_element(loctype, locvalue)
        select = Select(element)
        items = [i.text for i in select.options]
        if item not in items:
            raise ValueError(f"{item} is not present in the listbox")
        if isinstance(item, str):
            select.select_by_visible_text(item)
        else:
            select.select_by_index(item)

    def select_multiple_items(self, locator, items):
        locatortype, locatorvalue = locator
        lst_box = self.driver.find_element(locatortype, locatorvalue)
        select = Select(lst_box)
        for item in items:
            if isinstance(item, str):
                select.select_by_visible_text(item)
                time.sleep(1)
            else:
                select.select_by_index(item)
                time.sleep(1)

    def get_current_selected_item(self, locator):
        locatortype, locatorvalue = locator
        lst_box = self.driver.find_element(locatortype, locatorvalue)
        select = Select(lst_box)
        return select.first_selected_option.text

    def mouse_hover(self, locator):
        locatortype, locatorvalue = locator
        element = self.driver.find_element(locatortype, locatorvalue)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def send_keyboard_input(self, key):
        if not key.upper() in {'PAGE_DOWN', 'PAGE_UP', 'ENTER', 'ARROW_DOWN', 'ARROW_UP', 'ESCAPE'}:
            raise ValueError(f'Invalid Key passed {key}')
        actions = ActionChains(self.driver)
        if key.upper() == 'PAGE_DOWN':
            actions.send_keys(Keys.PAGE_DOWN).perform()
        elif key.upper() == 'PAGE_UP':
            actions.send_keys(Keys.PAGE_UP).perform()
        elif key.upper() == 'ENTER':
            actions.send_keys(Keys.ENTER).perform()
        elif key.upper() == 'ARROW_DOWN':
            actions.send_keys(Keys.ARROW_DOWN).perform()
        elif key.upper() == 'ARROW_UP':
            actions.send_keys(Keys.ARROW_UP).perform()
        elif key.upper() == 'ESCAPE':
            actions.send_keys(Keys.ESCAPE).perform()

    def close_application(self):
        self.driver.quit()
