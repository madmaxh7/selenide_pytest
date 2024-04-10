import re

from selene import be
from selene.core.exceptions import TimeoutException
from selenium.common import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, \
    ElementNotInteractableException, InvalidElementStateException

from base_object import BaseObject
import driver
import allure
import time
import datetime as dt


class BaseElement(BaseObject):

    def __init__(self):
        self.loc = None

    def click(self):
        with allure.step(f"Click {type(self).__name__}"):
            try:
                element = driver.selen_id.browser.element(css_or_xpath_or_by=self.loc)
                element.click()
            except (NoSuchElementException, TimeoutException):
                self.fail(f"Unable to find element {type(self).__name__}")
            except ElementClickInterceptedException as e:
                self.fail(f"Some element is blocking click on {type(self).__name__}: {str(e)}")
            except StaleElementReferenceException as e:
                self.fail(f"False Fail: {str(e)}")

    def send_keys(self, value):
        with allure.step(f"Type '{value}' on element {type(self).__name__}"):
            try:
                element = driver.selen_id.browser.element(css_or_xpath_or_by=self.loc)
                element.send_keys(value)
            except NoSuchElementException:
                self.fail(f"Unable to find element {type(self).__name__}")
            except ElementNotInteractableException:
                self.fail(f"Element {type(self).__name__} is not interactable")

    def clear(self):
        with allure.step(f"Clear {type(self).__name__}"):
            try:
                element = driver.selen_id.browser.element(css_or_xpath_or_by=self.loc)
                element.clear()
            except InvalidElementStateException:
                self.fail(f"Element {type(self).__name__} is not editable")

    @property
    def text(self):
        try:
            return driver.selen_id.browser.element(css_or_xpath_or_by=self.loc)().text
        except NoSuchElementException:
            self.fail(f"Unable to find element {type(self).__name__}")
        except StaleElementReferenceException:
            time.sleep(0.3)
            try:
                return driver.selen_id.browser.element(css_or_xpath_or_by=self.loc)().text
            except NoSuchElementException:
                self.fail(f"Unable to find element {type(self).__name__}")

    @property
    def rect(self):
        """
        returns dictionary with keys: 'x', 'y', 'height', 'width'
        """
        try:
            return driver.selen_id.browser.element(css_or_xpath_or_by=self.loc)().rect
        except NoSuchElementException:
            self.fail(f"Unable to find element {type(self).__name__}")

    @property
    def present(self):
        try:
            driver.selen_id.browser.element(css_or_xpath_or_by=self.loc).should(be.present)
            return True
        except Exception:
            return False

    @property
    def visible(self):
        try:
            return driver.selen_id.browser.element(css_or_xpath_or_by=self.loc).should(be.visible)
        except Exception:
            return False

    @property
    def id(self):
        return driver.selen_id.browser.element(css_or_xpath_or_by=self.loc)().get_attribute('id')

    def get_attribute(self, attr_name):
        try:
            return driver.selen_id.browser.element(css_or_xpath_or_by=self.loc)().get_attribute(attr_name)
        except NoSuchElementException:
            self.fail(f"Unable to find element {type(self).__name__}")
        except StaleElementReferenceException as e:
            try:
                time.sleep(0.1)
                return driver.selen_id.browser.element(css_or_xpath_or_by=self.loc)().get_attribute(attr_name)
            except NoSuchElementException:
                self.fail(f"Unable to find element {type(self).__name__} {e} ")

    def get_screenshot(self):
        return driver.selen_id.browser.element(css_or_xpath_or_by=self.loc)().screenshot_as_png

    def get_float_value(self):
        return float(re.sub(r"[^\d.]", "", self.text))

    def get_attribute_float_value(self, attr_name):
        return float(re.sub(r"[^\d.]", "", self.get_attribute(attr_name)))

    def wait_for_visible(self):
        with allure.step(f"Wait for {type(self).__name__} visible"):
            try:
                driver.selen_id.browser.element(css_or_xpath_or_by=self.loc).wait_until(be.visible)
            except TimeoutException:
                self.fail(f"Element {type(self).__name__} is not visible after timeout")

    def wait_for_present(self):
        with allure.step(f"Wait for {type(self).__name__} present"):
            try:
                driver.selen_id.browser.element(css_or_xpath_or_by=self.loc).wait_until(be.present)
            except TimeoutException:
                self.fail(f"Element {type(self).__name__} is not present after timeout")

    def wait_for_not_present(self):
        with allure.step(f"Wait for {type(self).__name__} not present"):
            try:
                driver.selen_id.browser.element(css_or_xpath_or_by=self.loc).wait_until(be.not_.present)
            except TimeoutException:
                self.fail(f"Element {type(self).__name__} is still present after timeout")

    def verify_present(self, present):
        with allure.step(f"Verify: element {type(self).__name__} is {'' if present else 'not '}present"):
            cur_present = self.present
            assert cur_present == present, (f"Element {type(self).__name__} present state"
                                            f"'{cur_present}' does not match expected '{present}'")

    def verify_visible(self, visible):
        with allure.step(f"Verify: element {type(self).__name__} is {'' if visible else 'not '}visible"):
            cur_visible = self.visible
            assert cur_visible == visible, (f"Element {type(self).__name__} visible state"
                                            f"'{cur_visible}' does not match expected '{visible}'")

    def verify_attribute_is_not(self, attr_name, value, get_err=False):
        with allure.step(f"Verify: attribute {attr_name} in element {type(self).__name__} is not '{value}'"):
            self.wait_for_present()
            cur_attr = self.get_attribute(attr_name)
            err = (f"Current attribute '{attr_name}' in element {type(self).__name__} value"
                   f"'{cur_attr}' matches '{value}'")
            try:
                assert cur_attr != value, err
            except AssertionError:
                if get_err:
                    return [err]
                else:
                    raise
            return []

    def verify_attribute_is(self, attr_name, value, get_err=False):
        with allure.step(f"Verify: attribute {attr_name} in element {type(self).__name__} is '{value}'"):
            self.wait_for_present()
            cur_attr = self.get_attribute(attr_name)
            err = (f"Current attribute '{attr_name}' in element {type(self).__name__} value"
                   f"'{cur_attr}' does not match expected '{value}'")
            try:
                assert cur_attr == value, err
            except AssertionError:
                if get_err:
                    return [err]
                else:
                    raise
            return []

    def verify_attribute_contains(self, attr_name, value, get_err=False):
        with allure.step(f"Verify: attribute {attr_name} in element {type(self).__name__} is '{value}'"):
            self.wait_for_present()
            cur_attr = str(self.get_attribute(attr_name))
            err = (f"Current attribute '{attr_name}' in element {type(self).__name__} value"
                   f"'{cur_attr}' does not match expected '{value}'")
            try:
                assert value in cur_attr, err
            except AssertionError:
                if get_err:
                    return [err]
                else:
                    raise
            return []

    def verify_text_is(self, value):
        with allure.step(f"Verify: text in element {type(self).__name__} is '{value}'"):
            self.wait_for_present()
            cur_text = self.text.strip()
            assert cur_text == value, (f"Current text in element {type(self).__name__}"
                                       f"'{cur_text}' does not match expected '{value}'")

    def verify_text_strip_is(self, value):
        with allure.step(f"Verify: text in element {type(self).__name__} is '{value}'"):
            self.wait_for_present()
            cur_text = self.text.strip()
            assert cur_text.strip() == value.strip(), (f"Current text in element {type(self).__name__}"
                                                       f"'{cur_text}' does not match expected '{value}'")

    def verify_attribute_strip_is(self, attr_name, value):
        with allure.step(f"Verify: attribute {attr_name} in element {type(self).__name__} is '{value}'"):
            self.wait_for_present()
            cur_attr = self.get_attribute(attr_name)
            assert cur_attr.strip() == value.strip(), (f"Current attribute '{attr_name}' in element"
                                                       f"{type(self).__name__} value '{cur_attr}'"
                                                       f"does not match expected '{value}'")

    def verify_text_in(self, values):
        with allure.step(f"Verify: text in element {type(self).__name__} is one of {values}"):
            self.wait_for_present()
            cur_text = self.text.strip()
            assert cur_text in values, (f"Current text in element {type(self).__name__}"
                                        f"'{cur_text}' does not match any of {values}")

    def verify_text_contains_one_of_values(self, values):
        with allure.step(f"Verify: text in element {type(self).__name__} contains one of values {values}"):
            self.wait_for_present()
            cur_text = self.text.strip()
            for val in values:
                if val in cur_text:
                    break
            else:
                self.fail(f"Current text '{cur_text}' does not contain any of values '{values}'")

    def verify_text_contains(self, value):
        with allure.step(f"Verify: text in element {type(self).__name__} contains '{value}'"):
            self.wait_for_present()
            cur_text = self.text.strip()
            assert value in cur_text, (f"Current text in element {type(self).__name__}"
                                       f"'{cur_text}' does not contain expected '{value}'")

    def verify_text_is_not(self, value):
        with allure.step(f"Verify: text in element {type(self).__name__} is not '{value}'"):
            self.wait_for_present()
            cur_text = self.text
            assert cur_text != value, f"Current text in element {type(self).__name__} '{cur_text}' matches '{value}'"

    def verify_is_date(self, date_format):
        with allure.step(f"Verify: text in element {type(self).__name__} has date format: {date_format}"):
            try:
                dt.datetime.strptime(re.sub(r'(\d)(st|nd|rd|th)', r'\1', self.text), date_format)
            except ValueError:
                self.fail(f'Current text in element {type(self).__name__} is not presented in format: {date_format}')


class BasePage(BaseObject):

    @allure.step("Wait")
    def wait(self, time_seconds):
        time.sleep(time_seconds)

    @property
    def window_size(self):
        """
        returns dictionary with keys 'width', 'height'
        """
        return driver.selen_id.window_size
