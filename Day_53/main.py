from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import requests

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(
    "https://docs.google.com/forms/d/e/1FAIpQLSfYJ_VrUrlDWU4_NlbNDqv64U_5nS9UlTc8BzrzCY7lVTSxpw/viewform?usp=sf_link")

price_list = []
addrs_list = []
links_list = []


def restart():
    reset = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    reset.click()


def adders(address):
    first_entry = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    first_entry.send_keys(address)


def price(money):
    second_entry = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second_entry.send_keys(money)


def link(href):
    third_entry = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third_entry.send_keys(href)


def submit():
    answer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    answer.click()


head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "110.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=
                        "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2"
                        "C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22eas"
                        "t%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.85787709831683"
                        "4%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D"
                        "%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%"
                        "3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value"
                        "%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7"
                        "D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%"
                        "7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%"
                        "22mapZoom%22%3A12%7D", headers=head
                        )
data = response.text

soup = BeautifulSoup(data, "html.parser")

data1 = soup.find_all("div", "bqsBln")
data2 = soup.find_all("a", "gdfTyO")

print(data1)
print(data2)

for i in data1:
    print(i.text)
    price_list.append(str(i.text))
for i in data2:
    print(i.text)
    addrs_list.append(str(i.text))
    print(i.get("href"))
    links_list.append(str(i.get('href')))


print(price_list, "\n", addrs_list, "\n", links_list)
print(len(price_list), "\n", len(addrs_list), "\n", len(links_list))
for i in range(len(price_list)):
    print(addrs_list[i])
    print(type(addrs_list[i]))


# first_entry.send_keys("hello")
# sleep(1.5)
# second_entry.send_keys("123")
# sleep(1.5)
# third_entry.send_keys("hello")
# sleep(1.5)
# submit.click()

for i in range(len(price_list)):
    sleep(3)
    main1 = addrs_list[i]
    adders(main1)
    sleep(1.5)
    main1 = price_list[i]
    price(main1)
    sleep(1.5)
    main1 = links_list[i]
    link(main1)
    sleep(1.5)
    submit()
    sleep(3)
    restart()


sleep(15)
