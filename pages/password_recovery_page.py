import allure

from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
from urls import FORGOT_PASSWORD_PAGE_URL


class PasswordRecoveryPage(BasePage):

    @allure.step("Открыть страницу восстановления пароля")
    def open_forgot_password_page(self):
        self.open(FORGOT_PASSWORD_PAGE_URL)

    def is_recover_button_displayed(self):
        return self.is_displayed(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    @allure.step("Ввести почту и нажать «Восстановить»")
    def recover_password(self, email):
        self.find_element(PasswordRecoveryPageLocators.EMAIL_INPUT).send_keys(email)
        self.click_element(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    def is_save_button_displayed(self):
        return self.is_displayed(PasswordRecoveryPageLocators.SAVE_BUTTON)

    @allure.step("Нажать на иконку показа пароля")
    def click_show_password_icon(self):
        self.click_element(PasswordRecoveryPageLocators.SHOW_PASSWORD_ICON)

    def is_password_field_active(self):
        field_class = self.find_element(PasswordRecoveryPageLocators.PASSWORD_FIELD).get_attribute("class")
        return "input_status_active" in field_class
