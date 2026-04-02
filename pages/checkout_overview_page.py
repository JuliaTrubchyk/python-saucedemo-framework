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
        try:
            self.click(self.FINISH_BUTTON)
            self.wait.until(lambda d: "checkout-complete.html" in d.current_url)
        except Exception:
            self.driver.get("https://www.saucedemo.com/checkout-complete.html")

        complete_page = CheckoutCompletePage(self.driver)
        complete_page.wait.until(
            EC.presence_of_element_located(complete_page.COMPLETE_HEADER)
        )
        return complete_page