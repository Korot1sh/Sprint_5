import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import Config
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from locators.main_page_locators import MainPageLocators


def login_user(driver):
    from data.test_data import TestData

    main_page = MainPage(driver)
    auth_page = AuthPage(driver)

    driver.get(Config.BASE_URL)
    main_page.open_login_form()

    auth_page.login(
        TestData.EXISTING_USER["email"],
        TestData.EXISTING_USER["password"]
    )

    WebDriverWait(driver, Config.TIMEOUT).until(
        EC.presence_of_element_located(MainPageLocators.LOGOUT_BUTTON)
    )

    return driver


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