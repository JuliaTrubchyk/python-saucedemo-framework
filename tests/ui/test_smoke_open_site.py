from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_success(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    page_title = inventory_page.get_page_title()
    assert page_title == "Products"