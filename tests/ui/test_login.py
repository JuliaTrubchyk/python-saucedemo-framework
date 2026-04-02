import pytest
from pages.login_page import LoginPage
from config import STANDARD_USERNAME, STANDARD_PASSWORD


@pytest.mark.smoke
def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = login_page.login_expect_success(STANDARD_USERNAME, STANDARD_PASSWORD)

    page_title = inventory_page.get_page_title()
    assert page_title == "Products"


@pytest.mark.regression
def test_inventory_items_are_displayed_after_login(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = login_page.login_expect_success(STANDARD_USERNAME, STANDARD_PASSWORD)

    items_count = inventory_page.get_inventory_items_count()
    assert items_count > 0

@pytest.mark.regression
def test_add_item_to_cart_updates_cart_badge(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = login_page.login_expect_success(STANDARD_USERNAME, STANDARD_PASSWORD)
    inventory_page.add_backpack_to_cart()

    cart_count = inventory_page.get_cart_badge_count()
    assert cart_count == "1"

@pytest.mark.regression
def test_cart_contains_added_item(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = login_page.login_expect_success(STANDARD_USERNAME, STANDARD_PASSWORD)
    inventory_page.add_backpack_to_cart()

    cart_page = inventory_page.open_cart_page()
    item_count = cart_page.get_cart_item_count()
    item_name = cart_page.get_cart_item_name()

    assert item_count == 1
    assert "Sauce Labs Backpack" in item_name

@pytest.mark.regression
def test_remove_item_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = login_page.login_expect_success(STANDARD_USERNAME, STANDARD_PASSWORD)
    inventory_page.add_backpack_to_cart()

    cart_page = inventory_page.open_cart_page()
    cart_page.remove_backpack_from_cart()

    item_count = cart_page.get_cart_item_count()
    assert item_count == 0

@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("standard_user", "wrong_pwd", "Username and password do not match"),
        ("standard_user", "", "Password is required"),
        ("", "secret_sauce", "Username is required"),
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
    ]
)

def test_login_negative_cases(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.submit_login(username, password)

    error_message = login_page.get_error_message()
    assert expected_error in error_message