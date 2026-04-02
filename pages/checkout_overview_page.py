from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.checkout_complete_page import CheckoutCompletePage

class CheckoutOverviewPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

        complete_page = CheckoutCompletePage(self.driver)
        complete_page.wait.until(
            EC.text_to_be_present_in_element(complete_page.COMPLETE_HEADER, "Thank you for your order!")
        )
        return complete_page