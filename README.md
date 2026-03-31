# Selenium Python Automation Framework (SauceDemo)

This project is a UI automation framework built using **Selenium + Python + pytest**.  
It demonstrates a complete end-to-end testing flow for the SauceDemo application.

---

## 🚀 Tech Stack

- Python
- Selenium WebDriver
- pytest
- Page Object Model (POM)

---

## 📁 Project Structure

```
python-saucedemo-framework/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests/
│   └── ui/
│       ├── test_login.py
│       └── test_checkout.py
│
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ✅ Implemented Test Scenarios

### 🔐 Login
- Successful login (smoke test)
- Invalid password
- Empty username
- Empty password
- Locked-out user

### 🛍️ Inventory
- Verify products are displayed after login

### 🛒 Cart
- Add item to cart
- Verify cart badge updates
- Verify item appears in cart
- Remove item from cart
- Verify cart is empty

### 💳 Checkout
- Navigate to checkout page
- Fill checkout information
- Continue to overview page
- Complete checkout
- Verify success message

---

## 🧪 Test Markers

- `@pytest.mark.smoke` → critical flow (login)
- `@pytest.mark.regression` → full test suite

Run only regression tests:

```bash
pytest -m regression
```

---

## 📸 Screenshot on Failure

The framework automatically captures screenshots when a test fails.

- Implemented using a pytest hook in `conftest.py`
- Screenshots are saved in the screenshots/ folder

---

## ▶️ How to Run Tests
1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Run all tests
```bash
pytest
```

---

## 🧠 Design Principles
- Page Object Model (POM)
- Reusable BasePage with common methods
- pytest fixtures for driver setup/teardown
- Data-driven testing using `@pytest.mark.parametrize`
- Clear separation between tests and page logic

---

## 📌 Notes

This project is designed as a learning and portfolio project to demonstrate UI automation skills and framework design for QA automation roles.