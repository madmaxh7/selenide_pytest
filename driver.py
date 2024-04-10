"""Webdriver"""
import allure
from selene import browser
from selene import by
from selenium import webdriver

import configs


class WebDriverWrapper:

    def __init__(self):
        self.driver = browser.config.driver
        self.browser = browser

    def connect(self):
        """Starting Webdriver"""
        if configs.web_driver_platform == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-infobars")
            options.add_argument("--enable-automation")
            options.add_argument("--headless")
            options.add_argument("--start-maximized")
            options.add_argument('--window-size=1920x1080')
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-setuid-sandbox")
        else:
            self.driver.quit()
            raise Exception("Unsupported webdriver platform platform %s" % configs.web_driver_platform)

    def disconnect(self):
        """Stop Webdriver"""
        self.driver.quit()

    def open_url(self, url):
        """Open url"""
        self.browser.open(url)

    def refresh(self):
        """Refresh current page"""
        self.driver.refresh()

    @allure.step("Execute script")
    def execute_script(self, script, *args):
        """Executes JavaScript in the current window/frame"""
        return self.driver.execute_script(script, *args)

    @property
    def window_size(self):
        """Gets the width and height of the current window."""
        return self.driver.get_window_size()

    def switch_to_frame(self, frame_loc):
        """Switches focus to the specified frame"""
        self.driver.switch_to.frame(self.get_element(frame_loc))

    def split_loc(self, loc):
        """Split locator"""
        str_by = loc[:loc.find('=')]
        str_value = loc[loc.find('=') + 1:]
        if str_by == "id":
            return by.id(str_value)
        elif str_by == "css":
            return by.css(str_value)
        else:
            return by.xpath(loc)

    def get_element(self, loc):
        """Find an element given a By strategy and locator"""
        be_in, value = self.split_loc(loc)
        return self.driver.find_element(be_in, value)

    def get_elements(self, loc):
        """Find an elements given a By strategy and locator"""
        be_in, value = self.split_loc(loc)
        return self.driver.find_elements(be_in, value)

    def get_element_id(self, loc):
        """Get an element id"""
        return self.get_element(loc).id

    def click(self, loc):
        """Click an element"""
        self.get_element(loc).click()

    def send_keys(self, loc, val):
        """Send text in element"""
        self.get_element(loc).send_keys(val)

    def clear(self, loc):
        """Clear field"""
        self.get_element(loc).clear()

    def get_rect(self, loc):
        """A dictionary with the size and location of the element."""
        return self.get_element(loc).rect

    def get_attribute(self, loc, attr_name):
        """Get a element attribute"""
        return self.get_element(loc).get_attribute(attr_name)


selen_id = WebDriverWrapper()
