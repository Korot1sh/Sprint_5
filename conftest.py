import pytest
from selenium import webdriver
from config import Config
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from data.test_data import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from helpers.generators import generate_user_data, generate_ad_data


@pytest.fixture
def driver():
    # Фикстура для создания и настройки драйвера
    options = webdriver.ChromeOptions()

    # Добавляем опции из конфига
    for option in Config.CHROME_OPTIONS:
        options.add_argument(option)

    driver = webdriver.Chrome(options=options)

    # Устанавливаем неявные ожидания
    driver.implicitly_wait(Config.IMPLICIT_WAIT)

    return driver


@pytest.fixture
def logged_in_driver(driver):
    # Фикстура для предварительно залогиненного пользователя
    main_page = MainPage(driver)
    auth_page = AuthPage(driver)

    # Логинимся
    driver.get(Config.BASE_URL)
    main_page.open_login_form()
    auth_page.login(
        TestData.EXISTING_USER["email"],
        TestData.EXISTING_USER["password"]
    )

    # Ждем подтверждения логина
    WebDriverWait(driver, Config.TIMEOUT).until(
        EC.presence_of_element_located(MainPageLocators.LOGOUT_BUTTON)
    )

    return driver


@pytest.fixture
def random_user():
    # Фикстура для генерации случайных данных пользователя
    return generate_user_data()


@pytest.fixture
def random_ad_data():
    # Фикстура для генерации случайных данных объявления
    return generate_ad_data()