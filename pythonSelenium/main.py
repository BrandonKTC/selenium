import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://www.linkedin.com/home")
# ID, Xpath, CSSSelector, Classname, name, linkText
# driver.find_element(By.ID, "session_key").send_keys("brandonkwamou@gmail.com")
# driver.find_element(By.ID, "session_password").send_keys("azertyuiop")
# driver.find_element(By.CLASS_NAME, "google-auth-button__placeholder").click()

# Xpath - //tagname[@attribute='value'] -> //input[@type='submit']
# CSS - //tagname[attribute='value'] -> //input[@type='submit'], #id, .classname
# driver.find_element(By.CSS_SELECTOR, "//input[name='name']").send_keys("Brandon")
# driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

