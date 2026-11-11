
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    @allure.step('Нажать на кнопку')
    def click_order_button(self, locator):
        self.click_element(locator)

    def click_button_logo_scooter(self):
        self.click_element(
            MainPageLocators.SCOOTER_LOGO
        )

    @allure.step('Нажать на кнопку')
    def click_button_logo_yandex(self):
        self.click_element(
            MainPageLocators.YANDEX_LOGO
        )

    @allure.step('Нажать на вопрос')
    def click_faq_question(self, locator):
        self.scroll_to_element(locator)
        self.wait.until(
        EC.element_to_be_clickable(locator)
        )
        self.click_element(locator)

    @allure.step('Получить ответ на выбранный вопрос')
    def get_faq_answer(self, locator, timeout=10):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text.replace('\u00a0', ' ').strip()
    
    @allure.step('Произошел переход страницу')
    def is_order_page_opened(self, url):
        return self.wait_for_url(url)
    
    @allure.step('Произошел переход страницу')
    def is_main_ya_opened(self, url):
        return self.wait_for_url(url)
