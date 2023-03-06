import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

dictionary = {}

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.python.org")

content1 = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li time")
content2 = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li a")

for i in content2:
    print(i.text)

