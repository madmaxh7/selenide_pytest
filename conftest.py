import pytest
import driver


@pytest.fixture(scope="function", autouse=False)
def driver_init(request):
    if 'webdriver' in request.keywords:
        driver.selen_id.connect()
        yield
        driver.selen_id.disconnect()
    else:
        yield
