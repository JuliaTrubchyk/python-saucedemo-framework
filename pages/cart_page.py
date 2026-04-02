from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


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
        return len(self.driver.find_elements(*self.CART_ITEM))

    def get_cart_item_name(self):
        return self.get_text(self.CART_ITEM_NAME)

    def remove_backpack_from_cart(self):
        button = self.wait.until(EC.presence_of_element_located(self.REMOVE_BACKPACK_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)

        # Wait until cart badge disappears
        self.wait.until(lambda d: len(d.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0)

    def checkout(self):
        self.wait_until_loaded()

        try:
            self.click(self.CHECKOUT_BUTTON)
            self.wait.until(lambda d: "checkout-step-one.html" in d.current_url)
        except Exception:
            self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

        checkout_page = CheckoutPage(self.driver)
        checkout_page.wait.until(
            EC.presence_of_element_located(checkout_page.FIRST_NAME_INPUT)
        )
        return checkout_page

