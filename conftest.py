import pytest
from selenium import webdriver

from config import Config
from data.test_data import TestData
from pages.main_page import MainPage
from pages.auth_page import AuthPage


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

    driver.get(Config.BASE_URL)
    main_page.open_login_form()

    auth_page.login(
        TestData.EXISTING_USER["email"],
        TestData.EXISTING_USER["password"]
    )

    main_page.wait_until_logged_in()

    return driver
