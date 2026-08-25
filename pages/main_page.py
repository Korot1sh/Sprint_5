from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def open(self):
        self.open_base_url()

    def open_login_form(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    def open_create_ad(self):
        self.click(MainPageLocators.CREATE_AD_BUTTON)

    def wait_until_logged_in(self):
        self.wait_for_element_visible(
            MainPageLocators.LOGOUT_BUTTON
        )