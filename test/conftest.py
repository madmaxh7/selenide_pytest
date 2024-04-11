"""
Conftest file
"""
import pytest
from pageobjects.web import constants
from pageobjects.web.base_page_en_element import HomePageEn
from pageobjects.web.login_page_element import LoginPage
from pageobjects.web.start_page_element import StartPage


@pytest.fixture
def login():
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
    return wiki_start_page, wiki_login_page, wiki_home_page
