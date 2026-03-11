import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_success(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    page_title = inventory_page.get_page_title()
    assert page_title == "Products"

@pytest.mark.regression
def test_login_invalid_password(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "wrong_pwd")

    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message
