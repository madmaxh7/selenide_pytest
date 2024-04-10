import allure
from selene import browser
from selene import by
from selenium import webdriver
from selenium.webdriver import ActionChains

import configs


class WebDriverWrapper(object):

    def __init__(self):
        self.driver = browser.config.driver
        self.browser = browser

    def connect(self):
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
        self.driver.quit()

    def open_url(self, url):
        self.browser.open(url)

    def refresh(self):
        self.driver.refresh()

    @allure.step("Execute script")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @property
    def window_size(self):
        return self.driver.get_window_size()

    def switch_to_frame(self, frame_loc):
        self.driver.switch_to.frame(self.get_element(frame_loc))

    def switch_to_dc(self):
        self.driver.switch_to.default_content()

    def split_loc(self, loc):
        str_by = loc[:loc.find('=')]
        str_value = loc[loc.find('=') + 1:]
        if str_by == "id":
            return by.id(str_value)
        elif str_by == "css":
            return by.css(str_value)
        else:
            return by.xpath(loc)

    def get_element(self, loc):
        be, value = self.split_loc(loc)
        return self.driver.find_element(be, value)

    def get_elements(self, loc):
        be, value = self.split_loc(loc)
        return self.driver.find_elements(be, value)

    def get_element_id(self, loc):
        return self.get_element(loc).id

    def click(self, loc):
        self.get_element(loc).click()

    def send_keys(self, loc, val):
        self.get_element(loc).send_keys(val)

    def clear(self, loc):
        self.get_element(loc).clear()

    def get_rect(self, loc):
        return self.get_element(loc).rect

    def get_attribute(self, loc, attr_name):
        return self.get_element(loc).get_attribute(attr_name)


selen_id = WebDriverWrapper()
