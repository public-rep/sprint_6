import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from conftest import *


class TestFAQ:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 10)

    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_text",
        [
            (
                MainPageLocators.FAQ_QUESTION_PRICE,
                MainPageLocators.FAQ_ANSWER_PRICE,
                faq_price_text
            ),
            (
                MainPageLocators.FAQ_QUESTION_LOTS_OF_SCOOTERS,
                MainPageLocators.FAQ_ANSWER_LOTS_OF_SCOOTERS,
                faq_lots_of_scooters_text
            ),
            (
                MainPageLocators.FAQ_QUESTION_PERIOD,
                MainPageLocators.FAQ_ANSWER_PERIOD,
                faq_period_text 
            ),
            (
                MainPageLocators.FAQ_QUESTION_TODAY,
                MainPageLocators.FAQ_ANSWER_TODAY,
                faq_today_text
            ),
            (
                MainPageLocators.FAQ_QUESTION_RENEWAL,
                MainPageLocators.FAQ_ANSWER_RENEWAL,
                faq_renewal_text

            ),
            (
                MainPageLocators.FAQ_QUESTION_POWER,
                MainPageLocators.FAQ_ANSWER_POWER,
                faq_power_text

            ),
            (
                MainPageLocators.FAQ_QUESTION_CANCEL,
                MainPageLocators.FAQ_ANSWER_CANCEL,
                faq_cancel_text

            ),
            (
                MainPageLocators.FAQ_QUESTION_OUT_OF_TOWN,
                MainPageLocators.FAQ_ANSWER_OUT_OF_TOWN,
                faq_out_of_town_text
            )
        ]
    )
    def test_faq_answers(
        self,
        question_locator,
        answer_locator,
        expected_text
    ):
        self.driver.get(main_url)
        page = MainPage(self.driver)

        page.click_faq_question(question_locator)

        actual = page.get_faq_answer(answer_locator)

        assert expected_text == actual

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
