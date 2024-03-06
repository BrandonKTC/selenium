import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

# Static Dropdown
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Female")

# Dynamic Dropdown
# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.find_element(By.ID, "autosuggest").send_keys("ind")
# time.sleep(2)
# countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
#
# for country in countries:
#     if country.text == "India":
#         country.click()
#         break
# time.sleep(2)

# Checkbox
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for option in checkboxes:
    if option.get_attribute("value") == "option2":
        option.click()
        time.sleep(3)
        break

# Radio Button
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radio_buttons[1].click()

time.sleep(2)