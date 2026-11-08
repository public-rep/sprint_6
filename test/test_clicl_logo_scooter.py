import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from conftest import *


class TestClickLogo:

    driver = None
    wait = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 10)

    @pytest.mark.parametrize(
        'url',
        [
            main_url,
            order_url
        ]
    )
    def test_click_logo_scooter(self, url):
        self.driver.get(url)

        page = MainPage(self.driver)
        page.click_button_logo_scooter()

        assert self.wait.until(EC.url_to_be(main_url))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
