import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from conftest import main_url, order_url


class TestOrderButton:

    driver = None
    wait = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 10)

    @pytest.mark.parametrize(
        'locator',
        [
            MainPageLocators.HEADER_ORDER_BUTTON,
            MainPageLocators.BOTTOM_ORDER_BUTTON
        ]
    )
    def test_click_order_button_redirects_to_order_page(self, locator):
        self.driver.get(main_url)

        page = MainPage(self.driver)

        page.click_order_button(locator)

        assert self.wait.until(EC.url_to_be(order_url))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()