def test_open_site(driver):
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title