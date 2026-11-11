import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import *
from constants import main_url
import allure

class TestFAQ:

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
    @allure.title('Проверка текста вопросов и ответов')
    def test_faq_answers(
        self,
        driver,
        question_locator,
        answer_locator,
        expected_text
    ):
        driver.get(main_url)
        page = MainPage(driver)

        page.click_faq_question(question_locator)

        actual = page.get_faq_answer(answer_locator)

        assert expected_text == actual