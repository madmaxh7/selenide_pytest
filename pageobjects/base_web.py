import allure
from selene.core.exceptions import TimeoutException
from selenium.common import NoSuchElementException

import driver
from base_web_page import BasePage
from pageobjects.base_web_element import BaseElement


class BaseWebElement(BaseElement):

    def mouse_over(self):
        with allure.step(f"Mouse over {type(self).__name__}"):
            try:
                driver.selen_id.mouse_over(self.loc)
            except (NoSuchElementException, TimeoutException):
                self.fail(f"Unable to find element {type(self).__name__}")

    def double_click(self):
        with allure.step(f"Double click {type(self).__name__}"):
            try:
                driver.selen_id.double_click(self.loc)
            except (NoSuchElementException, TimeoutException):
                self.fail(f"Unable to find element {type(self).__name__}")

    def scroll_into_view(self):
        with allure.step(f"Scroll into view {type(self).__name__}"):
            try:
                driver.selen_id.scroll_into_view(self.loc)
            except NoSuchElementException:
                self.fail(f"Unable to find element {type(self).__name__}")

    def click_js(self):
        with allure.step(f"Simulate click using js on {type(self).__name__}"):
            driver.selen_id.execute_script("arguments[0].click();", driver.selen_id.get_element(self.loc))

    def scroll(self, by_x=0, by_y=0):
        with allure.step(f"Scroll on {type(self).__name__} by ({by_x}, {by_y})"):
            driver.selen_id.execute_script(f"arguments[0].scrollBy({by_x},"
                                           f"{by_y});", driver.selen_id.get_element(self.loc))


class BaseWebPage(BasePage):

    @allure.step("Open URL")
    def open_url(self, url):
        driver.selen_id.open_url(url)

    @allure.step("Refresh")
    def refresh(self):
        driver.selen_id.refresh()

    @allure.step("Press key(s)")
    def type_keys(self, *keys):
        driver.selen_id.send_keys_ac(*keys)

    @allure.step("Scroll")
    def scroll(self, by_x=0, by_y=25):
        driver.selen_id.scroll_window(by_x, by_y)

    def wait_for_one_of_elements(self, els, timeout=30):
        with allure.step(f"Wait for one of elements is present: {', '.join([type(i).__name__ for i in els])}"):
            try:
                new_loc = "|".join([el.loc for el in els])
                driver.selen_id.wait_for_element_present(new_loc, timeout)
            except TimeoutException:
                self.fail(f"None of elements {', '.join([type(el).__name__ for el in els])}"
                          f" is present after {timeout} seconds")

    def wait_for_one_of_elements_visible(self, els, timeout=30):
        with allure.step(f"Wait for one of elements is visible: {', '.join([type(i).__name__ for i in els])}"):
            try:
                new_loc = "|".join([el.loc for el in els])
                driver.selen_id.wait_for_element_visible(new_loc, timeout)
            except TimeoutException:
                self.fail(f"None of elements {', '.join([type(el).__name__ for el in els])}"
                          f" is visible after {timeout} seconds")
