# Selenium Python Automation Framework

## Capstone Project

A Selenium WebDriver automation framework developed using Python for automating an E-Commerce web application.

### Application Under Test

Automation Exercise

https://automationexercise.com/

---

## Objective

The objective of this project is to design and develop a reusable Selenium Python automation framework using:

- Selenium WebDriver
- Python
- PyTest
- Unittest
- Page Object Model (POM)
- Utility Classes
- Configuration Management
- CSV Test Data
- Screenshots on Test Failure
- HTML Reporting

---

## Project Scenarios

### 1. Login

The framework automates:

1. Launch browser
2. Open Automation Exercise
3. Navigate to Login
4. Read login credentials from CSV
5. Enter email
6. Enter password
7. Click Login
8. Verify successful login

### 2. Product Search

The framework automates:

1. Launch browser
2. Navigate to Products
3. Read product name from CSV
4. Search for the product
5. Verify that the product is displayed

---

## Project Structure

```text
Capstone Project/
│
├── config/
│   └── config.ini
│
├── test_data/
│   └── test_data.example.csv
│
├── pages/
│   ├── login_page.py
│   └── products_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_product_search.py
│   └── test_unittest_login.py
│
├── utilities/
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── driver_factory.py
│   └── screenshot.py
│
├── screenshots/
│   └── test_screenshot_on_failure.png
│
├── reports/
│   └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
---

## Framework Components

### Page Object Model

Page-specific locators and actions are maintained separately from test cases using the Page Object Model (POM).

### Configuration Management

Application URL, browser and timeout values are maintained in `config.ini`.

### Test Data Management

Test data is maintained in CSV format and read using the CSV Reader utility.

### Driver Factory

The Driver Factory creates and configures the Selenium WebDriver.

### Screenshot on Failure

The framework automatically captures a screenshot when a PyTest test fails.

### HTML Reporting

PyTest HTML generates an execution report containing test results.

---

## Test Execution

### Prerequisites

- Python 3.x
- Google Chrome
- Internet connection

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate