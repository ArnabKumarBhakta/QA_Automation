import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For normal chrome testing setup 
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# if website protecte with bots
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    yield driver
    driver.quit()

def test_search_valid_product(driver):
    driver.get("https://demowebshop.tricentis.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "small-searchterms")))
    driver.find_element(By.ID, "small-searchterms").clear()
    driver.find_element(By.ID, "small-searchterms").send_keys("Smartphone")
    driver.find_element(By.CSS_SELECTOR, "input.button-1.search-box-button").click()
  

    products = driver.find_elements(By.CSS_SELECTOR, "h2.product-title")
    print(f"Found {len(products)} products")

    assert len(products) > 0, "No products found - Search failed!"
    print("✅ PASSED: Products displayed correctly!",flush=True)

def test_search_invalid_product(driver):
    driver.get("https://demowebshop.tricentis.com/")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "small-searchterms")))
    driver.find_element(By.ID, "small-searchterms").clear()
    driver.find_element(By.ID, "small-searchterms").send_keys("XYZ123NotExist")
    driver.find_element(By.CSS_SELECTOR, "input.button-1.search-box-button").click()

    # Wait for result page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.page-body, strong.result")))

    # This site shows "No products were found that matched your criteria"
    products = driver.find_elements(By.CSS_SELECTOR, "h2.product-title")
    
    # So check len == 0 OR text
    assert len(products) == 0, "Should be 0 products for invalid search!"
    print("✅ PASSED: Correct 'No products' message shown!", flush=True)
    
if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])