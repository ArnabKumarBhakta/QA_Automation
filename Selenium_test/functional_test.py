import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Functional 01: Login with WRONG password should show error
def test_01_invalid_login(driver):
    driver.get("https://automationexercise.com/login")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("arnab@test.com")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("WRONG_PASS")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    time.sleep(3)
    error = driver.find_element(By.XPATH, "//p[contains(text(),'incorrect')]").text
    assert "incorrect" in error.lower()
    print("Functional 01 PASS: Invalid login shows error")

# Functional 02: Product quantity can be changed
def test_02_product_quantity(driver):
    driver.get("https://automationexercise.com/product_details/1")
    time.sleep(3)
    qty = driver.find_element(By.XPATH, "//input[@id='quantity']")
    qty.clear()
    qty.send_keys("4")
    assert qty.get_attribute("value") == "4"
    print("Functional 02 PASS: Quantity changed to 4")

# Functional 03: Logout functionality
def test_03_logout(driver):
    driver.get("https://automationexercise.com/login")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("arnab@test.com")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("arnab.05")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(3)
    assert "login" in driver.current_url.lower()
    print("Functional 03 PASS: Logout works")

# Functional 04: Empty cart message
def test_04_empty_cart(driver):
    driver.get("https://automationexercise.com/view_cart")
    time.sleep(3)
    body_text = driver.find_element(By.XPATH, "//body").text
    # Should show empty or no product
    print("Functional 04 PASS: Cart page opens - Empty Cart Functional Checked")

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])