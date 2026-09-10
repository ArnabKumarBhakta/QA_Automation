from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
time.sleep(10)
print(f"Opening the  wesite : {driver.get} ")
driver.find_element(By.ID, "small-searchterms").send_keys("Apple MacBook Pro")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)