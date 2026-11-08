import pytest

from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.order_page import OrderPage
from pages.main_page import MainPage

from locators.order_page_locator import OrderPageLocators
from locators.main_page_locators import MainPageLocators

from conftest import main_url


class TestOrderPage:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Firefox()
        yield driver
        driver.quit()

    @pytest.mark.parametrize(
        "order_data",
        [
            {
                "name": "Иван",
                "surname": "Иванов",
                "address": "Москва, улица Ленина, 10",
                "metro": "Сокольники",
                "phone": "89991234567",
                "period": "сутки",
                "color": "black",
                "comment": "Позвонить перед доставкой"
            },
            {
                "name": "Петр",
                "surname": "Петров",
                "address": "Москва, улица Пушкина, 15",
                "metro": "Аэропорт",
                "phone": "89997654321",
                "period": "двое суток",
                "color": "grey",
                "comment": "Доставить после обеда"
            }
        ],
        ids=["first_user", "second_user"]
    )

    @pytest.mark.parametrize(
        "order_button",
        [
            MainPageLocators.HEADER_ORDER_BUTTON,
            MainPageLocators.BOTTOM_ORDER_BUTTON
        ],
        ids=["header_button", "bottom_button"]
    )

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

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                OrderPageLocators.NAME
            )
        )
        order_page.about_user_order(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )

        order_page.click_next_button()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                OrderPageLocators.DELIVERY_DATE
            )
        )

        delivery_date = (
            datetime.now() + timedelta(days=3)
        ).strftime("%d.%m.%Y")

        order_page.enter_delivery_date(delivery_date)

        order_page.select_rental_period(
            order_data["period"]
        )

        if order_data["color"] == "black":
            order_page.select_black_color()
        else:
            order_page.select_grey_color()

        order_page.enter_comment(
            order_data["comment"]
        )

        order_page.click_order_button()
        
        order_page.click_confirm_button()

        assert order_page.is_success_message_visible().is_displayed()