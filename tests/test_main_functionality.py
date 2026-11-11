import allure

from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Клик на «Конструктор» открывает конструктор")
    def test_constructor_link_opens_constructor(self, driver):
        # Переход из ленты обратно в конструктор
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        feed_page.click_constructor_link()

        assert MainPage(driver).is_constructor_displayed()

    @allure.title("Клик на «Лента заказов» открывает ленту")
    def test_feed_link_opens_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_feed_link()

        assert FeedPage(driver).is_feed_displayed()

    @allure.title("Клик на ингредиент открывает окно с деталями")
    def test_click_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_displayed()

    @allure.title("Окно с деталями закрывается кликом по крестику")
    def test_ingredient_modal_closes_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient()
        main_page.close_modal()

        assert main_page.is_modal_closed()

    @allure.title("Добавление ингредиента увеличивает его счётчик")
    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_before = main_page.get_sauce_counter()
        main_page.add_sauce_to_order()

        assert main_page.get_sauce_counter() == counter_before + 1

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_make_order(self, logged_in_driver):
        # Булка и соус в конструктор, оформление заказа
        main_page = MainPage(logged_in_driver)
        main_page.add_bun_to_order()
        main_page.add_sauce_to_order()
        main_page.click_order_button()

        assert main_page.get_order_number().isdigit()
