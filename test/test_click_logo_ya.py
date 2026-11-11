import pytest
from pages.main_page import MainPage
from constants import main_url, order_url
import allure


class TestClickLogo:

    @pytest.mark.parametrize(
        'url',
        [
            main_url,
            order_url
        ]
    )
    @allure.title('Проверка перехода на страницу яндекса при нажатие на логотип')
    def test_click_logo_yandex(self, driver,url):

        
        driver.get(url)

        page = MainPage(driver)
        
        page.click_button_logo_yandex()

        assert page.switch_to_new_window()

  