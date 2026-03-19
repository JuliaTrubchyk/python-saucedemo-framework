import os
from datetime import datetime

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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            file_name = f"{test_name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)