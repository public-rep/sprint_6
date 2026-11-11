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
    @allure.title('Проверка перехода на страницу самокат при нажатие на логотип')
    def test_click_logo_scooter(self,driver, url):
        
        driver.get(url)
        page = MainPage(driver)
        page.click_button_logo_scooter()
        assert page.is_main_ya_opened(main_url)

