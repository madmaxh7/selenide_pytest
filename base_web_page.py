import time
import allure
import driver
from base_object import BaseObject


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
