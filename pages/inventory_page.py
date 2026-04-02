from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_BACKPACK_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_inventory_items_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_TO_CART_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart_page(self):
        self.click(self.CART_ICON)
        return CartPage(self.driver)

