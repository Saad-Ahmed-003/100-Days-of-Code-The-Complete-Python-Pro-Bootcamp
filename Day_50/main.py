from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('geolocation', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://tinder.com")

sleep(2)

permission_1 = driver.find_element(By.XPATH, '//*[@id="o1400699221"]/div/div[2]/div/div/div[1]/div[1]/button')
permission_1.click()

log_in = driver.find_element(By.XPATH, '//*[@id="o1400699221"]/div/div[1]/div/main/div[1]/div/div/div/div/header/'
                                       'div/div[2]/div[2]/a')
log_in.click()

sleep(4)

fb_button = driver.find_element(By.XPATH, '//*[@id="o1622039657"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_button.click()

sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

output_number = driver.find_element(By.ID, "email")
output_number.send_keys("9665539971")

sleep(2)

output_password = driver.find_element(By.ID, "pass")
output_password.send_keys("saadbeta@212")
output_password.send_keys(Keys.ENTER)

sleep(3.5)

driver.switch_to.window(base_window)

sleep(7)

permission_2 = driver.find_element(By.XPATH, '//*[@id="o1622039657"]/main/div/div/div/div[3]/button[1]')


# age = driver.find_element(By.XPATH, '//*[@id="o1400699221"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/'
#                                     'div/div[2]/div[3]/div/div[1]/div/span[2]')

# print(age.text)

