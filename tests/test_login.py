from pages.main_page import MainPage
from pages.auth_page import AuthPage
from data.test_data import TestData
from config import Config


class TestLogin:
    def test_successful_login(self, driver):
        # Login пользователя
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.open(Config.BASE_URL)
        main_page.open_login_form()

        # Заполняем форму авторизации существующим пользователем
        auth_page.login(
            TestData.EXISTING_USER["email"],
            TestData.EXISTING_USER["password"]
        )

        # Проверяем успешный логин
        assert main_page.is_user_logged_in()
        assert main_page.is_logout_button_visible()
        assert "User." in main_page.get_user_name()