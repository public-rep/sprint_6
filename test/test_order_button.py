import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import *
from constants import main_url, order_url
import allure

class TestOrderButton:

    @pytest.mark.parametrize(
        'locator',
        [
            MainPageLocators.HEADER_ORDER_BUTTON,
            MainPageLocators.BOTTOM_ORDER_BUTTON
        ]
    )
    @allure.title('Проверка кнопок заказать')
    def test_click_order_button_redirects_to_order_page(self, driver,locator):
        
        driver.get(main_url)

        page = MainPage(driver)

        page.click_order_button(locator)

        assert page.is_order_page_opened(order_url)

 