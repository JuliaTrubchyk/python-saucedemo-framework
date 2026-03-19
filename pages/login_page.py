from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    # Locators
    BASE_URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(self.BASE_URL)

    # Actions
    def login(self, username, password):
        # Enter username
        self.type(self.USERNAME_INPUT, username)

        # Enter password
        self.type(self.PASSWORD_INPUT, password)

        # Click login button
        self.click(self.LOGIN_BUTTON)

        return InventoryPage(self.driver)



    # Page data
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)