import random


def generate_email():
    # Генерация случайного email
    return f"test_{random.randint(1000000000, 9999999999)}@gmail.com"


def generate_password():
    # Генерация случайного пароля
    return f"test_{random.randint(1000000000, 9999999999)}"


def generate_ad_title():
    # Генерация названия объявления
    return f"Test Ad {random.randint(1000, 9999)}"


def generate_ad_description():
    # Генерация описания объявления
    return f"Test Description {random.randint(1000, 9999)}"


def generate_price():
    # Генерация случайной цены
    return str(random.randint(100, 10000))


def generate_user_data():
    # Генерация данных случайного пользователя
    return {
        "email": generate_email(),
        "password": generate_password()
    }


def generate_ad_data():
    # Генерация данных случайного объявления
    return {
        "title": generate_ad_title(),
        "description": generate_ad_description(),
        "price": generate_price(),
        "condition": random.choice(["new", "used"])
    }