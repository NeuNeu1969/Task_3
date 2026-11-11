import allure

from data import ORDER_NUMBER_PLACEHOLDER
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import BASE_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(BASE_URL)

    def is_constructor_displayed(self):
        return self.is_displayed(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click_element(MainPageLocators.SAUCE)

    def is_ingredient_modal_displayed(self):
        return self.is_displayed(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Закрыть всплывающее окно крестиком")
    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    def is_modal_closed(self):
        return self.is_not_displayed(MainPageLocators.OPENED_MODAL)

    def get_sauce_counter(self):
        return int(self.get_text(MainPageLocators.SAUCE_COUNTER))

    @allure.step("Добавить соус в заказ")
    def add_sauce_to_order(self):
        self.drag_and_drop(MainPageLocators.SAUCE, MainPageLocators.BURGER_CONSTRUCTOR)

    @allure.step("Добавить булку в заказ")
    def add_bun_to_order(self):
        self.drag_and_drop(MainPageLocators.BUN, MainPageLocators.BURGER_CONSTRUCTOR)

    @allure.step("Нажать «Оформить заказ»")
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    def get_order_number(self):
        # Сначала в окне заглушка 9999, затем номер от сервера
        return self.wait_for_text_change(MainPageLocators.ORDER_NUMBER, ORDER_NUMBER_PLACEHOLDER)
