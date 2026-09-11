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

def test_01_website_opens(driver):
    driver.get("https://automationexercise.com")
    time.sleep(5)
    assert driver.title == "Automation Exercise"
    print("Test 01: Website opens successfully.")
def test_02_user_can_login(driver):
    driver.get("https://automationexercise.com/login")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("arnab@test.com")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("arnab.05")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    time.sleep(5)
    user=driver.find_element(By.XPATH, "//b[text()='Arnab']").text
    assert user == "Arnab"
    full_text = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]").text
    print(f"Test 02: User, {full_text}")

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])