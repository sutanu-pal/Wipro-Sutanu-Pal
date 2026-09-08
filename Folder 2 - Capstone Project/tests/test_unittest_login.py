import unittest

from pages.login_page import LoginPage
from utilities.csv_reader import CSVReader
from utilities.driver_factory import DriverFactory
from utilities.config_reader import ConfigReader


class TestLoginUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Read configuration
        cls.config = ConfigReader()

        # Create browser
        cls.driver = DriverFactory.create_driver()

        # Open application
        cls.driver.get(cls.config.get("base_url"))

        # Read test data
        test_data = CSVReader.read_data()[0]

        cls.email = test_data["username"]
        cls.password = test_data["password"]

    @classmethod
    def tearDownClass(cls):
        # Close browser
        cls.driver.quit()

    def test_valid_login_unittest(self):

        # Create Login Page object
        login_page = LoginPage(self.driver)

        # Navigate to Login page
        login_page.open_login_page()

        # Perform login
        login_page.login(self.email, self.password)

        # Verify successful login
        self.assertIn(
            "Logged in as",
            self.driver.page_source
        )


if __name__ == "__main__":
    unittest.main()