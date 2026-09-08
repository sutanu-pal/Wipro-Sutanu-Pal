from pages.products_page import ProductsPage
from utilities.csv_reader import CSVReader


class TestProductSearch:

    def test_search_product(self, driver):
        # Read test data from CSV
        test_data = CSVReader.read_data()[0]

        product_name = test_data["search_product"]

        # Create Products Page object
        products_page = ProductsPage(driver)

        # Navigate to Products page
        products_page.open_products_page()

        # Search for the product
        products_page.search_product(product_name)

        # Verify that the product is displayed
        assert products_page.is_product_displayed(product_name)