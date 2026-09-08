from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def create_driver():
        config = ConfigReader()

        browser = config.get("browser").lower()

        if browser == "chrome":
            options = Options()
            options.add_argument("--start-maximized")

            driver = webdriver.Chrome(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        return driver