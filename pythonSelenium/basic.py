from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# -- Chrome

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://google.com")
print(driver.title)
print(driver.current_url)
driver.refresh()
driver.minimize_window()
