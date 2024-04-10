import pytest
from base_web_page import BasePage
from pageobjects.web import constants
from pageobjects.web.home_page_en_element import HomePageEn
from pageobjects.web.login_page_element import LoginPage
from pageobjects.web.start_page_element import StartPage

pytestmark = [pytest.mark.webdriver,
              pytest.mark.usefixtures("driver_init", "open_home_page")]


class TestStartPage(BasePage):

    def test_select_en_language(self):
        wiki_page = StartPage()
        wiki_page.select_en_language_sp()

    def test_login_form_loading(self):
        wiki_start_page = StartPage()
        wiki_home_page = HomePageEn()
        wiki_login_page = LoginPage()
        wiki_start_page.select_en_language_sp()
        wiki_home_page.login_button.wait_for_present()
        wiki_home_page.login_button.click()
        wiki_login_page.fill_login_form(login=True)
        wiki_home_page.user_link.wait_for_present()
        user_name = wiki_home_page.user_link.text
        assert user_name == constants.USERNAME, (f"Current user name: '{user_name}' doesn't"
                                                 f"the same as expected '{constants.USERNAME}'")
