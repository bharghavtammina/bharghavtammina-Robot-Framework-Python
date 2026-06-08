"""Inspect Reporting page sidebar tree clicks."""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://transunit.traumasoft.com"
USERNAME = "rbane"
PASSWORD = "Jmi@2026"

opts = webdriver.ChromeOptions()
opts.add_argument("--headless=new")
opts.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 30)

driver.get(BASE_URL)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="login-username"]')))
driver.find_element(By.CSS_SELECTOR, '[data-testid="login-username"]').send_keys(USERNAME)
driver.find_element(By.CSS_SELECTOR, '[data-testid="login-password"]').send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, '[data-testid="login-submit"]').click()
wait.until(lambda d: d.current_url.rstrip("/") != BASE_URL.rstrip("/"))
time.sleep(2)

driver.get(f"{BASE_URL}/main.php?a=reporting:home")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#application_Tree_Container_QuickSearch")))
time.sleep(3)

billing = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(@class,'reporting_tree_module_header')][normalize-space()='Billing']")
    )
)
billing.click()
time.sleep(1)

aging = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='Aging By Current Payor']")
    )
)
aging.click()

try:
    wait.until(lambda d: "Aging By Current Payor" in d.find_element(By.ID, "application_Header_CurrentReport").text)
    print("SUCCESS:", driver.find_element(By.ID, "application_Header_CurrentReport").text)
except Exception as exc:
    print("FAIL:", exc)
    print("current:", driver.find_element(By.ID, "application_Header_CurrentReport").text)

driver.quit()
