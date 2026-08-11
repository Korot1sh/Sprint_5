from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import Config


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    def open_url(self, url):
        self.driver.get(url)

    def open_base_url(self):
        self.open_url(Config.BASE_URL)

    def wait_for_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait_for_element_visible(locator).click()

    def input_text(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)