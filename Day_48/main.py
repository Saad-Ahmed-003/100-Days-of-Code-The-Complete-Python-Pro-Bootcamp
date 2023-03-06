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

# for i in range(len(list1)):
#     print(i)
#     dictionary[i] = {"name": list2[i], "time": list1[i]}

for i in range(len(content1)):
    print(i)
    dictionary[i] = {"time": str(content1[i].text), "name": str(content2[i].text)}

print(dictionary)



