from pages.base_page import BasePage
from locators.create_ad_locators import CreateAdLocators


class CreateAdPage(BasePage):

    def wait_until_form_loaded(self):
        self.wait_for_element_visible(
            CreateAdLocators.TITLE_INPUT
        )

    def is_auth_modal_visible(self):
        try:
            return self.wait_for_element_visible(
                CreateAdLocators.AUTH_MODAL
            ).is_displayed()
        except:
            return False

    def select_category_books(self):
        self.click(CreateAdLocators.CATEGORY_DROPDOWN)
        self.click(CreateAdLocators.CATEGORY_OPTION_BOOKS)

    def select_city_spb(self):
        self.click(CreateAdLocators.CITY_DROPDOWN)
        self.click(CreateAdLocators.CITY_OPTION_SPb)

    def publish(self):
        self.click(CreateAdLocators.PUBLISH_BUTTON)
