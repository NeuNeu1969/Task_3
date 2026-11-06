import pytest
from selenium import webdriver

from helpers import generate_user_data, register_user, delete_user
from pages.login_page import LoginPage
from urls import BASE_URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    # Каждый тест запускается в Chrome и Firefox
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def user():
    # Пользователь создаётся через API и удаляется после теста
    user_data = generate_user_data()
    token = register_user(user_data)
    yield {"data": user_data, "token": token}
    delete_user(token)


@pytest.fixture
def logged_in_driver(driver, user):
    # Вход в аккаунт через страницу логина
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(user["data"]["email"], user["data"]["password"])
    # После входа открывается главная страница
    login_page.wait_for_url(BASE_URL + "/")
    return driver
