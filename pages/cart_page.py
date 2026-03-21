from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_item_count(self):
        cart_items = self.driver.find_elements(*self.CART_ITEM)
        return len(cart_items)

    def get_cart_item_name(self):
        return self.get_text(self.CART_ITEM_NAME)

    def remove_backpack_from_cart(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)

