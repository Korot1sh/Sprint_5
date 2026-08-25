from locators.create_ad_locators import CreateAdLocators


class CreateAdPage:

    def fill_ad_data(self, ad_data):
        self.input_text(
            CreateAdLocators.TITLE_INPUT,
            ad_data["title"]
        )
        self.input_text(
            CreateAdLocators.DESCRIPTION_INPUT,
            ad_data["description"]
        )
        self.input_text(
            CreateAdLocators.PRICE_INPUT,
            ad_data["price"]
        )

    def publish_ad(self):
        self.click(CreateAdLocators.PUBLISH_BUTTON)

    def select_category_books(self):
        self.click(CreateAdLocators.CATEGORY_DROPDOWN)
        self.click(CreateAdLocators.CATEGORY_OPTION_BOOKS)

    def select_city_spb(self):
        self.click(CreateAdLocators.CITY_DROPDOWN)
        self.click(CreateAdLocators.CITY_OPTION_SPb)