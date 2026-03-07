from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_login_success(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    page_title = driver.find_element(By.CLASS_NAME, "title").text
    assert page_title == "Products"