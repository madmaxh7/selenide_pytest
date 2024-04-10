import pytest

from base_object import BaseObject
from pageobjects.web.start_page_element import StartPage

pytestmark = [pytest.mark.usefixtures("driver_init", "open_home_page")]


class TestSmoke(BaseObject):

    def test_select_en_language(self):
        wiki_start_page = StartPage()
        wiki_start_page.language_select.select_en_language.wait_for_present()
