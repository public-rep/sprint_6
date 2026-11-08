from locators.main_page_locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_order_button(self, locator):
        button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(locator)
        )   
        self.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        button
        )
        button.click()

    def click_button_logo_scooter(self):
        self.driver.find_element(
            *MainPageLocators.SCOOTER_LOGO
        ).click()

    def click_button_logo_yandex(self):
        self.driver.find_element(
            *MainPageLocators.YANDEX_LOGO
        ).click()

    def click_faq_question(self, locator):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )
        button.click()

    def get_faq_answer(self, locator, timeout=10):
        panel = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        return panel.text.replace('\u00a0', ' ').strip()
