"""Inspect All Menus items after login."""
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://transunit.traumasoft.com"
USERNAME = "rbane"
PASSWORD = "Jmi@2026"

opts = webdriver.ChromeOptions()
opts.add_argument("--headless=new")
driver = webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 30)

driver.get(BASE_URL)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="login-username"]')))
driver.find_element(By.CSS_SELECTOR, '[data-testid="login-username"]').send_keys(USERNAME)
driver.find_element(By.CSS_SELECTOR, '[data-testid="login-password"]').send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, '[data-testid="login-submit"]').click()

wait.until(lambda d: d.current_url.rstrip("/") != BASE_URL.rstrip("/"))
time.sleep(3)

all_menus = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="All Menus"]')))
all_menus.click()
time.sleep(1)

items = driver.find_elements(By.CSS_SELECTOR, ".ts_menu_list_item")
print(f"menu items: {len(items)}")
for i, item in enumerate(items):
    if item.text.strip():
        print(f"  [{i}] text={item.text!r} aria-owns={item.get_attribute('aria-owns')}")

billing = driver.find_element(
    By.XPATH, "//div[contains(@class,'ts_menu_list_item')][normalize-space()='Billing']"
)
ActionChains(driver).move_to_element(billing).perform()
time.sleep(1)

billing_menu = driver.find_elements(By.CSS_SELECTOR, "#v-menu-13 .v-list-item")
print(f"\nBilling flyout (v-menu-13) items: {len(billing_menu)}")
for i, item in enumerate(billing_menu):
    text = item.text.strip()
    if text:
        print(f"  [{i}] text={text!r}")

workflow = driver.find_elements(
    By.CSS_SELECTOR, "#v-menu-13 a[href*='billing:workflow']"
)
if workflow:
    print(f"  Workflow link: {workflow[0].get_attribute('href')}")

billing.click()
time.sleep(1)

sub_items = driver.find_elements(
    By.CSS_SELECTOR, ".v-overlay--active .v-list-item, .v-menu__content .v-list-item"
)
print(f"\nsubmenu items after Billing click: {len(sub_items)}")
for i, item in enumerate(sub_items[:20]):
    print(f"  [{i}] text={item.text!r}")

driver.quit()
