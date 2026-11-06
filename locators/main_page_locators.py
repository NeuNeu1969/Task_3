from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    # Ингредиенты: первый соус и счётчик на его карточке
    SAUCE = (By.XPATH, "//h2[text()='Соусы']/following-sibling::ul[1]/a[1]")
    SAUCE_COUNTER = (By.XPATH, "//h2[text()='Соусы']/following-sibling::ul[1]/a[1]//p[contains(@class, 'counter_counter__num')]")
    BUN = (By.XPATH, "//h2[text()='Булки']/following-sibling::ul[1]/a[1]")
    BURGER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Всплывающие окна
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    OPENED_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button")
    ORDER_NUMBER = (By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2")
