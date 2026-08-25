from pages.main_page import MainPage
from pages.auth_page import AuthPage
from data.test_data import TestData
from config import Config
from helpers.generators import generate_user_data


class TestRegistration:
    def test_successful_registration(self, driver):
        # Регистрация пользователя
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.open(Config.BASE_URL)
        main_page.open_login_form()
        auth_page.go_to_registration()

        # Используем генератор для создания уникальных данных
        user_data = generate_user_data()
        auth_page.register(user_data["email"], user_data["password"])

        # Проверяем успешную регистрацию
        main_page.wait_until_logged_in()

        assert main_page.is_user_name_displayed()

    def test_registration_invalid_email(self, driver):
        # Регистрация с email не по маске
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.open(Config.BASE_URL)
        main_page.open_login_form()
        auth_page.go_to_registration()

        # Заполняем только email (невалидный)
        auth_page.input_email("invalid-email")
        auth_page.click_create_account()

        # Проверяем что остались на странице регистрации
        auth_page.wait_until_registration_page()

        assert auth_page.is_registration_page()

    def test_registration_existing_user(self, driver):
        # Регистрация уже существующего пользователя
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.open(Config.BASE_URL)
        main_page.open_login_form()
        auth_page.go_to_registration()

        # Используем существующие данные из test_data.py
        auth_page.register(
            TestData.EXISTING_USER["email"],
            TestData.EXISTING_USER["password"]
        )

        # Проверяем что остались на странице регистрации
        auth_page.wait_until_registration_page()

        assert auth_page.is_registration_page()