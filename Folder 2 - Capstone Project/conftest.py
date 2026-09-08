import os
import pytest

from utilities.driver_factory import DriverFactory
from utilities.config_reader import ConfigReader
from utilities.screenshot import ScreenshotUtility


@pytest.fixture
def driver(request):
    config = ConfigReader()

    driver = DriverFactory.create_driver()

    driver.get(config.get("base_url"))

    yield driver

    # Capture screenshot if the test failed
    if request.node.rep_call.failed:
        test_name = request.node.name
        ScreenshotUtility.capture(driver, test_name)

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)