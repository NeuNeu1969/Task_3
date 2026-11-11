from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    # Страница ввода почты
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # Страница ввода нового пароля
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/parent::div")
    SHOW_PASSWORD_ICON = (By.XPATH, "//label[text()='Пароль']/following-sibling::div[contains(@class, 'input__icon')]")
