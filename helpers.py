import random
import string

import requests

from urls import REGISTER_ENDPOINT, USER_ENDPOINT, INGREDIENTS_ENDPOINT, ORDERS_ENDPOINT


def generate_random_string(length):
    # Случайная строка из латинских букв
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_user_data():
    # Почта, пароль и имя пользователя
    return {
        "email": generate_random_string(10) + "@yandex.ru",
        "password": generate_random_string(10),
        "name": generate_random_string(10),
    }


def register_user(user_data):
    # Регистрация через API, возвращает токен
    response = requests.post(REGISTER_ENDPOINT, json=user_data)
    return response.json()["accessToken"]


def delete_user(token):
    # Удаление пользователя через API
    requests.delete(USER_ENDPOINT, headers={"Authorization": token})


def create_order(token):
    # Заказ из двух первых ингредиентов через API, возвращает номер
    ingredients = requests.get(INGREDIENTS_ENDPOINT).json()["data"][:2]
    payload = {"ingredients": [item["_id"] for item in ingredients]}
    response = requests.post(ORDERS_ENDPOINT, json=payload, headers={"Authorization": token})
    return response.json()["order"]["number"]
