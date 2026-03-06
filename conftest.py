import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Setup: create browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Give the driver to the test
    yield driver

    # Teardown: close browser (always runs, even if test fails)
    driver.quit()