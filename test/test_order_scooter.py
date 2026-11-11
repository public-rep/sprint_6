import pytest
from datetime import datetime, timedelta
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from constants import main_url
from data import * 
import allure



class TestOrderPage:

    @pytest.mark.parametrize(
        "order_data",
        order_data,
        ids=order_data_ids
    )

    @pytest.mark.parametrize(
        "order_button",
        [
            MainPageLocators.HEADER_ORDER_BUTTON,
            MainPageLocators.BOTTOM_ORDER_BUTTON
        ],
        ids=["header_button", "bottom_button"]
    )
    @allure.title('Проверка оформления заказа самоката по позитиву')
    def test_positive_order(
        self,
        driver,
        order_data,
        order_button
    ):

        driver.get(main_url)

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_button(order_button)


        order_page.about_user_order(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )

        order_page.click_next_button()



        delivery_date = (
            datetime.now() + timedelta(days=3)
        ).strftime("%d.%m.%Y")

        order_page.enter_delivery_date(delivery_date)

        order_page.select_rental_period(
            order_data["period"]
        )

        order_page.click_order_button()
        
        order_page.click_confirm_button()

        assert order_page.is_success_message_visible()