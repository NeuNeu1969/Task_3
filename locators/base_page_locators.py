from selenium.webdriver.common.by import By


class BasePageLocators:
    # Ссылки в шапке
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']")
    ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Затемнение при загрузке страницы
    LOADING_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal__P3_V5')]/div[contains(@class, 'Modal_modal_overlay')]")
