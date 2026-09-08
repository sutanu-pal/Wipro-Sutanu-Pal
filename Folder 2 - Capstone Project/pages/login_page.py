from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Locators
    LOGIN_PAGE_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-qa='login-button']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self):
        login_link = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_PAGE_LINK)
        )
        login_link.click()

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()