import pytest
from pages.login_page import LoginPage


@pytest.mark.regression
def test_user_can_open_checkout_page_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()

    cart_page = inventory_page.open_cart_page()
    checkout_page = cart_page.checkout()

    page_title = checkout_page.get_page_title()
    assert page_title == "Checkout: Your Information"


@pytest.mark.regression
def test_user_can_fill_checkout_information_and_continue(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()

    cart_page = inventory_page.open_cart_page()
    checkout_page = cart_page.checkout()

    checkout_page.fill_checkout_information("John", "Doe", "12345")
    checkout_page.continue_checkout()

    page_title = checkout_page.get_page_title()
    assert page_title == "Checkout: Overview"