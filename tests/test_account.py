import allure

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Личный кабинет")
class TestAccount:

    @allure.title("Клик на «Личный кабинет» открывает профиль")
    def test_account_link_opens_profile(self, logged_in_driver):
        MainPage(logged_in_driver).click_account_link()

        assert AccountPage(logged_in_driver).is_profile_page_opened()

    @allure.title("Переход в раздел «История заказов»")
    def test_order_history_link_opens_history(self, logged_in_driver):
        MainPage(logged_in_driver).click_account_link()
        account_page = AccountPage(logged_in_driver)
        account_page.click_order_history_link()

        assert account_page.is_order_history_opened()

    @allure.title("Выход из аккаунта открывает страницу входа")
    def test_logout_opens_login_page(self, logged_in_driver):
        MainPage(logged_in_driver).click_account_link()
        AccountPage(logged_in_driver).click_logout_button()

        assert LoginPage(logged_in_driver).is_login_page_displayed()
