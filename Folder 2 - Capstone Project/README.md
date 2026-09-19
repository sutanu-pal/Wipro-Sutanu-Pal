# Selenium Python Automation Framework

## 🧩 Capstone Project

A Selenium WebDriver automation framework developed using Python for automating an E-Commerce web application.

### 🎯 Application Under Test

**Automation Exercise**
https://automationexercise.com/

---

## 📄 Project Report

The complete project report is available as a PDF document.

📄 [View Report](./Capstone%20Proj%20Report.pdf)

## 🎥 Demonstration Video

The complete project demonstration video is available on Google Drive. The video demonstrates the framework structure, Page Object Model, utility classes, test data management, login automation, product search automation, Unittest, PyTest execution, HTML reporting, and screenshot capture on failure.

🔗 [Watch Project Demonstration Video](https://drive.google.com/file/d/1JZVRopVR7nSRjYEk3pEha_d0gAEBlS6F/view?usp=sharing)

---

## 🛠️ Objective

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

## 📋 Project Scenarios

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

## 🏗️ Project Structure

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
```

---

## ⚙️ Framework Components

### 📄 Page Object Model

Page-specific locators and actions are maintained separately from test cases using the Page Object Model (POM).

The page objects include:

- `LoginPage` – handles login page elements and actions.
- `ProductsPage` – handles product navigation and product search operations.

This improves code readability, reusability, and maintainability.

### 🔧 Configuration Management

Application URL, browser, and timeout values are maintained in:

```text
config/config.ini
```

The `ConfigReader` utility reads these configuration values during test execution.

### 📊 Test Data Management

Test data is maintained separately in CSV format.
The `CSVReader` utility reads login credentials and product search data from the CSV file.

The test data contains:

- Username
- Password
- Product name

### 🏭 Driver Factory

The `DriverFactory` is responsible for creating and configuring the Selenium WebDriver.
It provides a centralized way to initialize the browser used by the automation tests.

### 🧰 Utility Classes

Reusable utility classes are used to handle common framework operations and keep the test cases clean and maintainable.

The utility classes include:

- `ConfigReader` – reads configuration values from `config.ini`.
- `CSVReader` – reads test data from CSV files.
- `DriverFactory` – creates and configures the Selenium WebDriver.
- `ScreenshotUtility` – captures screenshots when PyTest tests fail.

These utilities can be reused across multiple test cases and help reduce duplicate code.

### 🧪 Unittest

Unittest is used to implement and execute a separate login test case using Python's built-in `unittest` framework.

The Unittest test case is implemented in:

```text
tests/test_unittest_login.py
```

It uses `setUpClass()` for test setup, `tearDownClass()` for browser cleanup, and Unittest assertions for test validation.

### 🧪 PyTest

PyTest is used as the primary test execution framework for running the automation test cases.

The PyTest test cases are implemented in:

```text
tests/test_login.py
tests/test_product_search.py
```

PyTest provides test discovery, assertions, fixtures, and test execution capabilities for the framework.

### 📸 Screenshot on Failure

The framework automatically captures a screenshot when a PyTest test fails.

Screenshots are saved in:

```text
screenshots/
```

The screenshot utility helps in identifying and debugging failures during test execution.

### 📈 HTML Reporting

The framework uses `pytest-html` to generate an HTML test execution report.

The generated report is available at:

```text
reports/report.html
```

The report provides the execution status of the automated test cases, including passed and failed tests.

---

## ▶️ Test Execution

### ✅ Prerequisites

- Python 3.x
- Google Chrome
- Internet connection

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd "Capstone Project"
```

### 2️⃣ Create Virtual Environment

Windows:

```bash
python -m venv venv
```

macOS / Linux:

```bash
python3 -m venv venv
```

### 3️⃣ Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure Test Settings

Update the base URL, browser, and timeout values in:

```text
config/config.ini
```

### 6️⃣ Update Test Data

Add or update credentials and search values in:

```text
test_data/test_data.example.csv
```

### 7️⃣ Run Tests

Run all PyTest test cases:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_login.py
```

Run Unittest test cases:

```bash
python -m unittest tests/test_unittest_login.py
```

---

## 📑 Test Reports

After execution, the HTML report is generated in:

```text
reports/report.html
```

Failure screenshots are automatically saved in:

```text
screenshots/
```

and linked inside the HTML report.

---

## 🧰 Tech Stack

| Tool / Library      | Purpose                          |
|----------------------|-----------------------------------|
| Python               | Core programming language         |
| Selenium WebDriver   | Browser automation                |
| PyTest               | Test execution framework          |
| Unittest             | Alternate test execution framework|
| pytest-html          | HTML report generation            |
| configparser         | Reading `config.ini`              |
| csv                  | Data-driven test inputs           |

---

## 📌 Notes

- This framework follows the Page Object Model to separate locators and page logic from test scripts, improving readability and maintainability.
- The framework can be extended by adding new page objects, test cases, and CSV data sets as the application grows.

---

## 📄 License

This project is intended for educational and portfolio purposes.