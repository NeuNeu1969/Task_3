import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import LOGIN_PAGE_URL


class LoginPage(BasePage):

    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open(LOGIN_PAGE_URL)

    @allure.step("Войти в аккаунт")
    def login(self, email, password):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Нажать «Восстановить пароль»")
    def click_recover_password_link(self):
        self.click_element(LoginPageLocators.RECOVER_PASSWORD_LINK)

    def is_login_page_displayed(self):
        return self.is_displayed(LoginPageLocators.LOGIN_TITLE)
