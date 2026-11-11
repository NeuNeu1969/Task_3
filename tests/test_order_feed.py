import allure

from helpers import create_order
from locators.feed_page_locators import FeedPageLocators
from pages.account_page import AccountPage
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик на заказ открывает окно с деталями")
    def test_click_order_opens_details_modal(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        feed_page.click_first_order()

        assert feed_page.is_order_modal_displayed()

    @allure.title("Заказы из «Истории заказов» отображаются в ленте")
    def test_user_orders_from_history_shown_in_feed(self, logged_in_driver, user):
        # Заказ пользователя через API, номер из истории заказов
        create_order(user["token"])
        MainPage(logged_in_driver).click_account_link()
        account_page = AccountPage(logged_in_driver)
        account_page.click_order_history_link()
        order_number = account_page.get_order_numbers()[0]
        account_page.click_feed_link()

        assert FeedPage(logged_in_driver).is_order_in_feed(order_number)

    @allure.title("Новый заказ увеличивает счётчик «Выполнено за всё время»")
    def test_new_order_increases_total_counter(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        total_before = feed_page.get_total_counter()
        create_order(user["token"])

        assert feed_page.wait_for_counter_increase(FeedPageLocators.TOTAL_COUNTER, total_before) > total_before

    @allure.title("Новый заказ увеличивает счётчик «Выполнено за сегодня»")
    def test_new_order_increases_today_counter(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        today_before = feed_page.get_today_counter()
        create_order(user["token"])

        assert feed_page.wait_for_counter_increase(FeedPageLocators.TODAY_COUNTER, today_before) > today_before

    @allure.title("Номер нового заказа появляется в разделе «В работе»")
    def test_new_order_number_shown_in_work(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        order_number = create_order(user["token"])

        assert feed_page.is_order_in_work(str(order_number))
