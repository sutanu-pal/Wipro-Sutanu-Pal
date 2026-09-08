from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    # Locators
    PRODUCTS_LINK = (By.CSS_SELECTOR, "a[href='/products']")
    SEARCH_PRODUCT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_products_page(self):
        products_link = self.wait.until(
            EC.element_to_be_clickable(self.PRODUCTS_LINK)
        )
        products_link.click()

    def search_product(self, product_name):
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_PRODUCT)
        )

        search_box.clear()
        search_box.send_keys(product_name)

        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )

        search_button.click()

    def is_product_displayed(self, product_name):
        product_locator = (
            By.XPATH,
            f"//div[contains(@class,'productinfo')]//p[normalize-space()='{product_name}']"
        )

        try:
            self.wait.until(
                EC.visibility_of_element_located(product_locator)
            )
            return True
        except:
            return False