from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout_complete_page import CheckoutCompletePage
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

        complete_page = CheckoutCompletePage(self.driver)
        complete_page.wait.until(
            EC.presence_of_element_located(complete_page.COMPLETE_HEADER)
        )
        return complete_page