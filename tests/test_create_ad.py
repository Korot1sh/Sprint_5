from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.create_ad_page import CreateAdPage
from data.test_data import TestData


class TestCreateAd:

    def test_create_ad_unauthorized(self, driver):
        # Создание объявления неавторизованным пользователем
        main_page = MainPage(driver)
        create_ad_page = CreateAdPage(driver)

        main_page.open()
        main_page.open_create_ad()

        # Проверяем что появилось модальное окно авторизации
        assert create_ad_page.is_auth_modal_visible()

    def test_create_ad_authorized(self, driver):
        # Создание объявления авторизованным пользователем
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)
        create_ad_page = CreateAdPage(driver)

        # Логинимся
        main_page.open()
        main_page.open_login_form()
        auth_page.login(
            TestData.EXISTING_USER["email"],
            TestData.EXISTING_USER["password"]
        )

        # Ждем пока пользователь залогинится
        main_page.wait_until_logged_in()

        # Создаем объявление
        main_page.open_create_ad()

        # Ждем загрузки формы создания объявления
        create_ad_page.wait_until_form_loaded()

        # Используем генератор для создания уникальных данных объявления
        ad_data = TestData.generate_ad_data()

        create_ad_page.fill_ad_data(ad_data)

        # Публикуем (состояние оставляем по умолчанию - "Новый")
        create_ad_page.publish_ad()

        # Выбор категории и города
        create_ad_page.select_category_books()
        create_ad_page.select_city_spb()