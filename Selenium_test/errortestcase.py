from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1) Open Web Browser (Chrome)
driver = webdriver.Chrome()
driver.maximize_window()
# time.sleep(10)

# 2) Open URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
time.sleep(5)
print("Running TC_002 - Invalid Password Test")


# 3) Enter username (Admin)
driver.find_element(By.NAME,"username").send_keys("Admin")

# 4) Enter password (Wrong123)
driver.find_element(By.NAME,"password").send_keys("Wrong123")

# 5) Click on Login
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)


error = driver.find_element(By.CSS_SELECTOR, "p.oxd-alert-content-text").text
print(f"Error Message Found: {error}")

if error == "Invalid credentials":
    print("TC_002 PASS - Invalid credentials error is displayed")
else:
    print("TC_002 FAIL")

driver.quit()