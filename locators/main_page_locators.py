from selenium.webdriver.common.by import By


class MainPageLocators:

    HEADER_ORDER_BUTTON = (
        By.XPATH, "//button[text()='Заказать']"
    )
    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton')]//button"
    )
    FAQ_QUESTION_PRICE = (
        By.ID, "accordion__heading-0"
    )
    FAQ_ANSWER_PRICE = (
        By.CSS_SELECTOR, "#accordion__panel-0 p"
    )
    FAQ_QUESTION_LOTS_OF_SCOOTERS = (
        By.ID, "accordion__heading-1"
    )
    FAQ_ANSWER_LOTS_OF_SCOOTERS = (
        By.CSS_SELECTOR, "#accordion__panel-1 p"
    )
    FAQ_QUESTION_PERIOD = (
        By.ID, "accordion__heading-2"
    )
    FAQ_ANSWER_PERIOD= (
        By.CSS_SELECTOR, "#accordion__panel-2 p"
    )
    FAQ_QUESTION_TODAY = (
        By.ID, "accordion__heading-3"
    )
    FAQ_ANSWER_TODAY = (
        By.CSS_SELECTOR, "#accordion__panel-3 p"
    )
    FAQ_QUESTION_RENEWAL= (
        By.ID, "accordion__heading-4"
    )
    FAQ_ANSWER_RENEWAL = (
        By.CSS_SELECTOR, "#accordion__panel-4 p"
    )
    FAQ_QUESTION_POWER= (
        By.ID, "accordion__heading-5"
    )
    FAQ_ANSWER_POWER = (
        By.CSS_SELECTOR, "#accordion__panel-5 p"
    )
    FAQ_QUESTION_CANCEL = (
        By.ID, "accordion__heading-6"
    )
    FAQ_ANSWER_CANCEL = (
        By.CSS_SELECTOR, "#accordion__panel-6 p"
    )
    FAQ_QUESTION_OUT_OF_TOWN = (
        By.ID, "accordion__heading-7"
    )
    FAQ_ANSWER_OUT_OF_TOWN = (
        By.CSS_SELECTOR, "#accordion__panel-7 p"
    )
    YANDEX_LOGO = (
        By.XPATH, '//img[@alt="Yandex"]'
    )
    SCOOTER_LOGO = (
        By.XPATH,
        "//a[contains(@class,'Header_LogoScooter')]"
    )