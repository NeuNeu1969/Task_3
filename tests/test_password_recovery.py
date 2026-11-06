import allure

from data import RECOVERY_EMAIL
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Кнопка «Восстановить пароль» открывает страницу восстановления")
    def test_recover_password_link_opens_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_recover_password_link()

        assert PasswordRecoveryPage(driver).is_recover_button_displayed()

    @allure.title("Ввод почты и клик «Восстановить» открывает ввод нового пароля")
    def test_recover_password_with_email_opens_reset_page(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_forgot_password_page()
        recovery_page.recover_password(RECOVERY_EMAIL)

        assert recovery_page.is_save_button_displayed()

    @allure.title("Клик по иконке показа пароля подсвечивает поле")
    def test_show_password_icon_makes_field_active(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_forgot_password_page()
        recovery_page.recover_password(RECOVERY_EMAIL)
        recovery_page.click_show_password_icon()

        assert recovery_page.is_password_field_active()
