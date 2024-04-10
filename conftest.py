"""
Conftest file
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import driver


@pytest.fixture(scope="function", autouse=False)
def driver_init(request):
    driver.selen_id.connect()

    yield
    driver.selen_id.disconnect()
