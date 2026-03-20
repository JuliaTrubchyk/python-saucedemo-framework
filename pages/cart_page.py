from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_LIST = (By.CLASS_NAME, "cart_list")

    def get_cart_item_count(self):
        cart_items = self.driver.find_elements(*self.CART_ITEM)
        return len(cart_items)


