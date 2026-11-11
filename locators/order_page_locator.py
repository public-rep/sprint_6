
from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")

    METRO_OPTIONS = (By.CSS_SELECTOR, ".select-search__select div")

    NEXT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Далее']"
    )


    DELIVERY_DATE = (
        By.CSS_SELECTOR,
        "input[placeholder='* Когда привезти самокат']"
    )

    RENTAL_PERIOD = (By.CSS_SELECTOR, ".Dropdown-control")
    RENTAL_PERIOD_OPTIONS = (By.CSS_SELECTOR, ".Dropdown-option")

    BLACK_COLOR = (
        By.XPATH,
        "//label[contains(., 'чёрный жемчуг')]"
    )

    GREY_COLOR = (
        By.XPATH,
        "//label[contains(., 'серая безысходность')]"
    )

    COMMENT = (
        By.CSS_SELECTOR,
        "input[placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.CSS_SELECTOR,
    "button.Button_Middle__1CSJM:nth-child(2)"
    )

    CONFIRM_BUTTON = (
    By.XPATH,
    "//div[contains(@class, 'Order_Modal')]//button[normalize-space()='Да']"
    )

    CONFIRM_MODAL = (
        By.CSS_SELECTOR,
        ".Order_Modal__YZ-d3"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(), 'Заказ оформлен')]"
    )

    DATEPICKER = (
        By.CSS_SELECTOR,
        ".react-datepicker"
    )
