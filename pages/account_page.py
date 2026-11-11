import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from urls import PROFILE_PAGE_URL, ORDER_HISTORY_PAGE_URL


class AccountPage(BasePage):

    def is_profile_page_opened(self):
        self.find_element(AccountPageLocators.PROFILE_LINK)
        return self.wait_for_url(PROFILE_PAGE_URL) == PROFILE_PAGE_URL

    @allure.step("Перейти в «Историю заказов»")
    def click_order_history_link(self):
        self.click_element(AccountPageLocators.ORDER_HISTORY_LINK)

    def is_order_history_opened(self):
        return self.wait_for_url(ORDER_HISTORY_PAGE_URL) == ORDER_HISTORY_PAGE_URL

    @allure.step("Выйти из аккаунта")
    def click_logout_button(self):
        self.click_element(AccountPageLocators.LOGOUT_BUTTON)

    def get_order_numbers(self):
        return self.get_texts(AccountPageLocators.ORDER_NUMBERS)
