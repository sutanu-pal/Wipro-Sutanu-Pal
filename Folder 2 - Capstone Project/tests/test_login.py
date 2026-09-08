from pages.login_page import LoginPage
from utilities.csv_reader import CSVReader


class TestLogin:

    def test_valid_login(self, driver):
        # Read test data from CSV
        test_data = CSVReader.read_data()[0]

        email = test_data["username"]
        password = test_data["password"]

        # Create Login Page object
        login_page = LoginPage(driver)

        # Navigate to Login page
        login_page.open_login_page()

        # Perform login
        login_page.login(email, password)

        # Verify successful login
        assert "Logged in as" in driver.page_source