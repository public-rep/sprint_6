import pytest

from datetime import datetime, timedelta
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()



