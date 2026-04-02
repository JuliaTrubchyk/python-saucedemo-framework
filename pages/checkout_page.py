from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout_overview_page import CheckoutOverviewPage
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

        overview_page = CheckoutOverviewPage(self.driver)
        overview_page.wait.until(
            EC.presence_of_element_located(overview_page.FINISH_BUTTON)
        )
        return overview_page