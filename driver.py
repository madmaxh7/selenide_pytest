"""Webdriver"""
import allure
from selene import by
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WebDriverWrapper:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--enable-automation")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-setuid-sandbox")
        self.chrome_driver = webdriver.Chrome(options=options, service=ChromeService())

    def disconnect(self):
        """Stop WebDriver"""
        self.chrome_driver.quit()

    def open_url(self, url):
        """Open URL"""
        self.chrome_driver.get(url)

    def refresh(self):
        """Refresh current page"""
        self.chrome_driver.refresh()

    @allure.step("Execute script")
    def execute_script(self, script, *args):
        """Executes JavaScript in the current window/frame"""
        return self.chrome_driver.execute_script(script, *args)

    @property
    def window_size(self):
        """Gets the width and height of the current window."""
        return self.chrome_driver.get_window_size()

    def switch_to_frame(self, frame_loc):
        """Switches focus to the specified frame"""
        self.chrome_driver.switch_to.frame(self.get_element(frame_loc))

    @staticmethod
    def split_loc(loc):
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
        method, value = self.split_loc(loc)
        return self.chrome_driver.find_element(method, value)

    def get_elements(self, loc):
        """Find an elements given a By strategy and locator"""
        method, value = self.split_loc(loc)
        return self.chrome_driver.find_elements(method, value)

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
        """Get an element attribute"""
        return self.get_element(loc).get_attribute(attr_name)

    def wait_for_element_visible(self, loc, timeout):
        wdw = WebDriverWait(self.chrome_driver, timeout, ignored_exceptions=[WebDriverException])
        method, value = self.split_loc(loc)
        return wdw.until(expected_conditions.visibility_of_element_located((method, value)),
                         "Element '%s' not visible after '%s' seconds" % (loc, timeout))

    def wait_for_element_present(self, loc, timeout):
        wdw = WebDriverWait(self.chrome_driver,
                            timeout,
                            ignored_exceptions=[WebDriverException])
        method, value = self.split_loc(loc)
        return wdw.until(expected_conditions.presence_of_element_located((method, value)),
                         "Element '%s' not found after '%s' seconds" % (loc, timeout))

    def wait_for_element_not_present(self, loc, timeout):
        wdw = WebDriverWait(self.chrome_driver, timeout, ignored_exceptions=[WebDriverException])
        method, value = self.split_loc(loc)
        return wdw.until(expected_conditions.invisibility_of_element((method, value)),
                         "Element '%s' still present after '%s' seconds" % (loc, timeout))

selen_id = WebDriverWrapper()
