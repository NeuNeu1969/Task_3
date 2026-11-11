# Адрес сервиса
BASE_URL = "https://stellarburgers.education-services.ru"

# Страницы
LOGIN_PAGE_URL = BASE_URL + "/login"
FORGOT_PASSWORD_PAGE_URL = BASE_URL + "/forgot-password"
RESET_PASSWORD_PAGE_URL = BASE_URL + "/reset-password"
PROFILE_PAGE_URL = BASE_URL + "/account/profile"
ORDER_HISTORY_PAGE_URL = BASE_URL + "/account/order-history"
FEED_PAGE_URL = BASE_URL + "/feed"

# Ручки API для подготовки данных
REGISTER_ENDPOINT = BASE_URL + "/api/auth/register"
USER_ENDPOINT = BASE_URL + "/api/auth/user"
INGREDIENTS_ENDPOINT = BASE_URL + "/api/ingredients"
ORDERS_ENDPOINT = BASE_URL + "/api/orders"
