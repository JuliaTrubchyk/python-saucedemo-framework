from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.checkout_complete_page import CheckoutCompletePage


class CheckoutOverviewPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
        self.wait.until(EC.url_contains("checkout-complete.html"))
        return CheckoutCompletePage(self.driver)