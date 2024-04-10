import pytest

import configs
from pageobjects.web.start_page_element import StartPage


@pytest.fixture
def open_home_page():
    start_page = StartPage()
    start_page.open_url(configs.base_url_web)
