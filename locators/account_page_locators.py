from selenium.webdriver.common.by import By


class AccountPageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_NUMBERS = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox')]/p[1]")
