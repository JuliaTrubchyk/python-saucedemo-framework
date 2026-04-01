import pytest
from pages.login_page import LoginPage
from config import STANDARD_USERNAME, STANDARD_PASSWORD


@pytest.mark.regression
def test_user_can_open_checkout_page_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)
    inventory_page.add_backpack_to_cart()

    cart_page = inventory_page.open_cart_page()
    checkout_page = cart_page.checkout()

    page_title = checkout_page.get_page_title()
    assert page_title == "Checkout: Your Information"


@pytest.mark.regression
def test_user_can_fill_checkout_information_and_continue(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)
    inventory_page.add_backpack_to_cart()

    cart_page = inventory_page.open_cart_page()
    checkout_page = cart_page.checkout()

    checkout_page.fill_checkout_information("John", "Doe", "12345")
    overview_page = checkout_page.continue_checkout()

    page_title = overview_page.get_page_title()
    assert page_title == "Checkout: Overview"

@pytest.mark.regression
def test_user_can_complete_checkout(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)
    inventory_page.add_backpack_to_cart()

    cart_page = inventory_page.open_cart_page()
    checkout_page = cart_page.checkout()

    checkout_page.fill_checkout_information("John", "Doe", "12345")
    overview_page = checkout_page.continue_checkout()

    complete_page = overview_page.finish_checkout()

    complete_header = complete_page.get_complete_header()
    assert complete_header == "Thank you for your order!"


