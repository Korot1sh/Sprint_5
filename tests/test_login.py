from pages.main_page import MainPage


class TestLogin:
    def test_successful_login(self, logged_in_driver):
        # Login пользователя
        main_page = MainPage(logged_in_driver)

        # Заполняем форму авторизации существующим пользователем

        # Проверяем успешный логин
        assert main_page.is_user_logged_in()