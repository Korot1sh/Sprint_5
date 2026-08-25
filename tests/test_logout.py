from pages.main_page import MainPage


class TestLogout:

    def test_login_register_button_displayed_after_logout(self, logged_in_driver):
        # Logout пользователя
        main_page = MainPage(logged_in_driver)

        # Сначала логинимся

        # Проверяем что залогинены
        main_page.wait_until_logged_in()

        # Затем разлогиниваемся
        main_page.logout()

        # Проверяем что вышли (появилась кнопка входа)
        main_page.wait_until_logged_out()

        assert main_page.is_login_register_button_displayed()

    def test_logout_button_absent_after_logout(self, logged_in_driver):
        # Logout пользователя
        main_page = MainPage(logged_in_driver)

        # Сначала логинимся

        # Проверяем что залогинены
        main_page.wait_until_logged_in()

        # Затем разлогиниваемся
        main_page.logout()

        # Проверяем что вышли (появилась кнопка входа)
        main_page.wait_until_logged_out()

        # Проверяем что кнопка выхода исчезла
        assert main_page.is_logout_button_absent()