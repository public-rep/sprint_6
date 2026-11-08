
from selenium.webdriver.common.by import By
from locators.order_page_locator import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_name(self, name):
        self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.NAME
            )
        ).send_keys(name)

    def enter_surname(self, surname):
        self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.SURNAME
            )
        ).send_keys(surname)

    def enter_address(self, address):
        self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.ADDRESS
            )
        ).send_keys(address)

    def enter_metro(self, metro):
        metro_input = self.wait.until(
            EC.element_to_be_clickable(
                OrderPageLocators.METRO
            )
        )

        metro_input.send_keys(metro)

        options = self.wait.until(
            EC.visibility_of_all_elements_located(
                OrderPageLocators.METRO_OPTIONS
            )
        )

        for option in options:
            if metro in option.text:
                option.click()
                return

        raise AssertionError(
            f"Станция метро {metro} не найдена"
        )

    def enter_phone(self, phone):
        self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.PHONE
            )
        ).send_keys(phone)

    def about_user_order(
        self, name, surname, address, metro, phone
    ):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_metro(metro)
        self.enter_phone(phone)

    def click_next_button(self):
        self.wait.until(
            EC.element_to_be_clickable(
                OrderPageLocators.NEXT_BUTTON
            )
        ).click()

    def enter_delivery_date(self, date):
        date_input = self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.DELIVERY_DATE
            )
        )

        date_input.click()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ESCAPE)

        self.wait.until(
            EC.invisibility_of_element_located(
                OrderPageLocators.DATEPICKER
            )
        )

    def select_rental_period(self, period):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                OrderPageLocators.RENTAL_PERIOD
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            dropdown
        )

        dropdown.click()

        options = self.wait.until(
            EC.visibility_of_all_elements_located(
                OrderPageLocators.RENTAL_PERIOD_OPTIONS
            )
        )

        for option in options:
            if option.text.strip() == period:
                option.click()
                return

        raise AssertionError(
            f"Срок аренды '{period}' не найден"
        )

    def select_black_color(self):
        self.wait.until(
            EC.element_to_be_clickable(
                OrderPageLocators.BLACK_COLOR
            )
        ).click()

    def select_grey_color(self):
        self.wait.until(
            EC.element_to_be_clickable(
                OrderPageLocators.GREY_COLOR
            )
        ).click()

    def enter_comment(self, comment):
        self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.COMMENT
            )
        ).send_keys(comment)

    def click_order_button(self):
        order_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        order_button.click()


    def click_confirm_button(self):
        confirm_button = self.wait.until(
        EC.element_to_be_clickable(
            OrderPageLocators.CONFIRM_BUTTON
            )
        )

        confirm_button.click()

    def is_confirm_modal_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.CONFIRM_MODAL
            )
        )

    def is_success_message_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.SUCCESS_MESSAGE
            )
        )
