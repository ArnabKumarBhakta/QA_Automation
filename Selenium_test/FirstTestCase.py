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

# 3) Enter username (Admin)
driver.find_element(By.NAME,"username").send_keys("Admin")

# 4) Enter password (admin123)
driver.find_element(By.NAME,"password").send_keys("admin123")

# 5) Click on Login
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# 6) Capture title of the home page (Actual title)
actual_title = driver.title
print("Actual Title is:", actual_title)

# 7) Verify title of the page: OrangeHRM (Expected)
excepted_title="OrangeHRM"

if actual_title==excepted_title:
    print("Test Pass")
else:
    print("Test Fail")


driver.close()
