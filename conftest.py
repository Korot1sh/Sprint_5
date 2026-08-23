import pytest
from selenium import webdriver

from config import Config
from helpers.generators import login_user


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
    return login_user(driver)