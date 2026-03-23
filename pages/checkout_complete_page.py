from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_complete_header(self):
        return self.get_text(self.COMPLETE_HEADER)