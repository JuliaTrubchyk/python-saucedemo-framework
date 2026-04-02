from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def wait_until_loaded(self):
        self.wait.until(EC.presence_of_element_located(self.CART_LIST))

    def get_cart_item_count(self):
        self.wait_until_loaded()
        cart_items = self.driver.find_elements(*self.CART_ITEM)
        return len(cart_items)

    def get_cart_item_name(self):
        return self.get_text(self.CART_ITEM_NAME)

    def remove_backpack_from_cart(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)
        self.wait.until(lambda d: len(d.find_elements(*self.CART_ITEM)) == 0)

    def checkout(self):
        self.wait_until_loaded()
        self.click(self.CHECKOUT_BUTTON)

        checkout_page = CheckoutPage(self.driver)
        checkout_page.wait.until(
            EC.presence_of_element_located(checkout_page.FIRST_NAME_INPUT)
        )
        return checkout_page

