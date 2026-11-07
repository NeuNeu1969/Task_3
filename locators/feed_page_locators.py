from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    FIRST_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]")
    ORDER_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]")
    ORDER_MODAL_COMPOSITION = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//p[text()='Cостав']")
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_WORK_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")
