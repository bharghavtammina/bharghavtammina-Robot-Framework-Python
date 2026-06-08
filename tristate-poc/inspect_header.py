"""Inspect header Reporting nav after login."""
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
time.sleep(3)

for el in driver.find_elements(By.XPATH, "//button[normalize-space()='Reporting']"):
    if el.is_displayed():
        print("HEADER BTN:", el.get_attribute("outerHTML")[:300])

header_reporting = None
for el in driver.find_elements(By.XPATH, "//button[normalize-space()='Reporting']"):
    if el.is_displayed() and el.rect["y"] < 200:
        header_reporting = el
        break

if header_reporting:
    header_reporting.click()
    time.sleep(1)
    for el in driver.find_elements(By.CSS_SELECTOR, ".v-overlay--active a, .v-menu__content a"):
        if el.is_displayed():
            print("DROPDOWN LINK:", repr(el.text.strip()), el.get_attribute("href"))

driver.quit()
