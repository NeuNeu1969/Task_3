import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_page_locators import BasePageLocators

# Перетаскивание через события браузера: обычный drag and drop не работает в Firefox
DRAG_AND_DROP_SCRIPT = """
const source = arguments[0];
const target = arguments[1];
const dataTransfer = new DataTransfer();
const events = [[source, 'dragstart'], [target, 'dragenter'], [target, 'dragover'], [target, 'drop'], [source, 'dragend']];
for (const [element, type] of events) {
    element.dispatchEvent(new DragEvent(type, {bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
}
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_loading(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(BasePageLocators.LOADING_OVERLAY))

    def click_element(self, locator):
        self.wait_for_loading()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            # В Firefox затемнение может появиться уже после ожидания
            self.wait_for_loading()
            element.click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def is_not_displayed(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))
        return self.driver.current_url

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.driver.execute_script(DRAG_AND_DROP_SCRIPT, source, target)

    @allure.step("Перейти в конструктор")
    def click_constructor_link(self):
        self.click_element(BasePageLocators.CONSTRUCTOR_LINK)

    @allure.step("Перейти в ленту заказов")
    def click_feed_link(self):
        self.click_element(BasePageLocators.FEED_LINK)

    @allure.step("Перейти в личный кабинет")
    def click_account_link(self):
        self.click_element(BasePageLocators.ACCOUNT_LINK)
