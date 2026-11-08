import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from conftest import main_url, order_url


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
    def test_click_logo_yandex(self, url):
        self.driver.get(url)

        page = MainPage(self.driver)

        original_window = self.driver.current_window_handle

        page.click_button_logo_yandex()

        self.wait.until(EC.number_of_windows_to_be(2))

        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

        assert self.wait.until(EC.url_contains('ya.ru'))

        self.driver.close()
        self.driver.switch_to.window(original_window)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()