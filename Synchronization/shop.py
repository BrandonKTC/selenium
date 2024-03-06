import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service = Service()
driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/')
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)
assert count > 0

for product in results:
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
time.sleep(2)
select = Select(driver.find_element(By.XPATH, "//select"))
select.select_by_visible_text("France")
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
time.sleep(4)
