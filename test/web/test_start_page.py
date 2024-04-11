import pytest
from base_web_page import BasePage
from pageobjects.web import constants
from pageobjects.web.base_page_en_element import HomePageEn
from pageobjects.web.login_page_element import LoginPage
from pageobjects.web.personal_page import PersonalPage
from pageobjects.web.start_page_element import StartPage

pytestmark = [pytest.mark.usefixtures("open_home_page")]


class TestStartPage(BasePage):
    @pytest.mark.gui_tests
    def test_select_en_language(self):
        wiki_page = StartPage()
        wiki_page.select_en_language_sp()

    @pytest.mark.gui_tests
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

    @pytest.mark.gui_tests
    def test_login_form_loading(self, login):
        w_home_pg = login[2]
        personal_pg = PersonalPage()
        search_text = constants.SEARCH_TEXT[0]
        title = list(search_text.keys())[0]
        description = search_text[title]
        w_home_pg.search_field.send_keys(search_text.keys())
        w_home_pg.search_result(title).description().wait_for_present()
        w_home_pg.search_result(title).description().verify_text_is(description)
        w_home_pg.search_result(list((constants.SEARCH_TEXT[0]).keys())[0]).click()
        personal_pg.persona_title.verify_text_is(title)
