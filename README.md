# Task_3: UI-тесты Stellar Burgers

Автотесты веб-приложения https://stellarburgers.education-services.ru (Selenium + pytest + Allure).
Тесты запускаются в Google Chrome и Mozilla Firefox.

## Покрытие

- Восстановление пароля
- Личный кабинет
- Основной функционал: конструктор, лента заказов, окно ингредиента, счётчик, оформление заказа
- Раздел «Лента заказов»

## Структура

- `pages/` Page Object, класс на страницу, общие методы в `base_page.py`
- `locators/` локаторы, файл на страницу
- `tests/` тесты, класс на раздел; фикстуры в `conftest.py`
- `urls.py`, `data.py`, `helpers.py` адреса, данные, создание пользователя и заказа через API
- `allure_results/` результаты для Allure-отчёта

## Запуск

```
pip install -r requirements.txt
pytest tests/ --alluredir=allure_results
allure serve allure_results
```

## Особенности

- Тестовый пользователь создаётся через API перед тестом и удаляется после.
- Ингредиенты перетаскиваются через JavaScript: обычный drag and drop не работает в Firefox.
