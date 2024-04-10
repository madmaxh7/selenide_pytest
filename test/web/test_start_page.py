import pytest
from base_web_page import BasePage
from pageobjects.web.start_page_element import StartPage

pytestmark = [pytest.mark.webdriver,
              pytest.mark.usefixtures("driver_init", "open_home_page")]


class TestStartPage(BasePage):

    def test_select_en_language(self):
        wiki_page = StartPage()
        wiki_page.select_en_language_sp()

    def test_login_form_loading(self):
        wiki_page = StartPage()
        wiki_page.select_en_language_sp()
