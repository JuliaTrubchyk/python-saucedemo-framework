from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        # Wait until username field is visible, then type username
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)

        # Type password
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        # Click login button
        self.driver.find_element(*self.LOGIN_BUTTON).click()