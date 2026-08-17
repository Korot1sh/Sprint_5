from pages.main_page import MainPage
from pages.auth_page import AuthPage
from data.test_data import TestData
from config import Config


class TestLogout:
    def test_successful_logout(self, driver):
        # Logout пользователя
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        # Сначала логинимся
        main_page.open(Config.BASE_URL)
        main_page.open_login_form()
        auth_page.login(
            TestData.EXISTING_USER["email"],
            TestData.EXISTING_USER["password"]
        )

        # Проверяем что залогинены
        main_page.wait_until_logged_in()

        # Затем разлогиниваемся
        main_page.logout()

        # Проверяем что вышли (появилась кнопка входа)
        main_page.wait_until_logged_out()

        assert main_page.is_login_register_button_displayed()
        # Проверяем что кнопка выхода исчезла
        assert main_page.is_logout_button_absent()