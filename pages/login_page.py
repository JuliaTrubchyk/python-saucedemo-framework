from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")


    def login(self, username, password):
        # Enter username
        self.type(self.USERNAME_INPUT, username)

        # Enter password
        self.type(self.PASSWORD_INPUT, password)

        # Click login button
        self.click(self.LOGIN_BUTTON)