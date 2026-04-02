import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()

    headless = os.getenv("HEADLESS") == "true"

    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # Create driver
    driver = webdriver.Chrome(options=options)

    # Set consistent window size for both local and CI
    driver.set_window_size(1920, 1080)

    # Provide driver to tests
    yield driver

    # Teardown
    driver.quit()