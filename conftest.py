import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    options = Options()

    headless = os.getenv("HEADLESS") == "true"

    # Reduce Chrome noise (important for CI stability)
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    options.add_argument("--disable-notifications")

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    # Consistent viewport for local + CI
    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()


# Hook: runs after each test phase
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only capture failures during test execution
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name

            # Save screenshot
            screenshot_file = os.path.join(
                screenshots_dir, f"{test_name}_{timestamp}.png"
            )
            driver.save_screenshot(screenshot_file)

            # Save HTML page source
            html_file = os.path.join(
                screenshots_dir, f"{test_name}_{timestamp}.html"
            )
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(driver.page_source)