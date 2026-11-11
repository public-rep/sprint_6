
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    @allure.step('Открыть браузер')
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Нажать на элемент')
    def click_element(self, locator):        
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        element.click()
    @allure.step('Найти элемант')
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step('Найти поле ввода')
    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Получить текст элемента')
    def get_element_text(self, locator):
        return self.find_element(locator).text.replace(
            '\u00a0', ' '
        ).strip()

    @allure.step('Проверить url')
    def wait_for_url(self, url):
        return self.wait.until(
            EC.url_to_be(url)
        )
    
    @allure.step('Переключается на новую вкладку')
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(2)
        )

        self.driver.switch_to.window(
        self.driver.window_handles[1]
        )

        return WebDriverWait(self.driver, 10).until(
            EC.url_contains('ya.ru')
        )
    
    @allure.step('Прокрутка')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)

        self.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        element
        )