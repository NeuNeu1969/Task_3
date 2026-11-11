import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
from urls import FEED_PAGE_URL


class FeedPage(BasePage):

    @allure.step("Открыть ленту заказов")
    def open_feed_page(self):
        self.open(FEED_PAGE_URL)

    def is_feed_displayed(self):
        return self.is_displayed(FeedPageLocators.FEED_TITLE)

    @allure.step("Кликнуть на заказ в ленте")
    def click_first_order(self):
        self.click_element(FeedPageLocators.FIRST_ORDER)

    def is_order_modal_displayed(self):
        return self.is_displayed(FeedPageLocators.ORDER_MODAL_COMPOSITION)

    def is_order_in_feed(self, order_number):
        # Номер в ленте с решёткой и нулями, например #0618
        return self.wait_for_text_in_element(FeedPageLocators.ORDER_LIST, order_number)

    def get_counter(self, locator):
        # Счётчик приходит с сервера не сразу, до этого на странице 0
        return int(self.wait_for_text_change(locator, "0"))

    def get_total_counter(self):
        return self.get_counter(FeedPageLocators.TOTAL_COUNTER)

    def get_today_counter(self):
        return self.get_counter(FeedPageLocators.TODAY_COUNTER)

    def wait_for_counter_increase(self, locator, old_value):
        return self.wait_for_number_increase(locator, old_value)

    def is_order_in_work(self, order_number):
        return self.wait_for_text_in_element(FeedPageLocators.IN_WORK_LIST, order_number)
