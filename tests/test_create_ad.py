from pages.main_page import MainPage
from pages.create_ad_page import CreateAdPage
from helpers.generators import generate_ad_data


class TestCreateAd:

    def test_create_ad_unauthorized(self, driver):
        # Создание объявления неавторизованным пользователем
        main_page = MainPage(driver)
        create_ad_page = CreateAdPage(driver)

        main_page.open()
        main_page.open_create_ad()

        # Проверяем что появилось модальное окно авторизации
        assert create_ad_page.is_auth_modal_visible()

    def test_create_ad_authorized(self, logged_in_driver):
        # Создание объявления авторизованным пользователем
        main_page = MainPage(logged_in_driver)

        # Ждем пока пользователь залогинится
        main_page.wait_until_logged_in()
        assert main_page.is_user_logged_in()

    def test_create_ad_form(self, logged_in_driver):
        # Создание объявления авторизованным пользователем
        main_page = MainPage(logged_in_driver)
        create_ad_page = CreateAdPage(logged_in_driver)

        # Ждем пока пользователь залогинится
        main_page.wait_until_logged_in()

        # Создаем объявление
        main_page.open_create_ad()

        # Ждем загрузки формы создания объявления
        create_ad_page.wait_until_form_loaded()
        assert create_ad_page.is_form_visible()

    def test_create_ad_data(self, logged_in_driver):
        # Создание объявления авторизованным пользователем
        main_page = MainPage(logged_in_driver)
        create_ad_page = CreateAdPage(logged_in_driver)

        # Ждем пока пользователь залогинится
        main_page.wait_until_logged_in()

        # Создаем объявление
        main_page.open_create_ad()

        # Ждем загрузки формы создания объявления
        create_ad_page.wait_until_form_loaded()

        # Используем генератор для создания уникальных данных объявления
        ad_data = generate_ad_data()

        create_ad_page.fill_ad_data(ad_data)
        assert create_ad_page.is_ad_data_filled(ad_data)

    def test_create_ad_category(self, logged_in_driver):
        # Создание объявления авторизованным пользователем
        main_page = MainPage(logged_in_driver)
        create_ad_page = CreateAdPage(logged_in_driver)

        # Ждем пока пользователь залогинится
        main_page.wait_until_logged_in()

        # Создаем объявление
        main_page.open_create_ad()

        # Ждем загрузки формы создания объявления
        create_ad_page.wait_until_form_loaded()

        # Используем генератор для создания уникальных данных объявления
        ad_data = generate_ad_data()

        create_ad_page.fill_ad_data(ad_data)

        create_ad_page.select_category_books()
        assert create_ad_page.is_books_category_selected()

    def test_create_ad_city(self, logged_in_driver):
        # Создание объявления авторизованным пользователем
        main_page = MainPage(logged_in_driver)
        create_ad_page = CreateAdPage(logged_in_driver)

        # Ждем пока пользователь залогинится
        main_page.wait_until_logged_in()

        # Создаем объявление
        main_page.open_create_ad()

        # Ждем загрузки формы создания объявления
        create_ad_page.wait_until_form_loaded()

        # Используем генератор для создания уникальных данных объявления
        ad_data = generate_ad_data()

        create_ad_page.fill_ad_data(ad_data)
        create_ad_page.select_category_books()

        create_ad_page.select_city_spb()
        assert create_ad_page.is_spb_city_selected()

    def test_create_ad_publish(self, logged_in_driver):
        # Создание объявления авторизованным пользователем
        main_page = MainPage(logged_in_driver)
        create_ad_page = CreateAdPage(logged_in_driver)

        # Ждем пока пользователь залогинится
        main_page.wait_until_logged_in()

        # Создаем объявление
        main_page.open_create_ad()

        # Ждем загрузки формы создания объявления
        create_ad_page.wait_until_form_loaded()

        # Используем генератор для создания уникальных данных объявления
        ad_data = generate_ad_data()

        create_ad_page.fill_ad_data(ad_data)

        # Публикуем (состояние оставляем по умолчанию - "Новый")
        create_ad_page.publish_ad()