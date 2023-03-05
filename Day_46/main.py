from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.amazon.in/gp/product/B0B5V8NT52/ref=ox_sc_act_title_1?smid=A14CZOWI0VEHLG&psc=1"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '110.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7'
}

response = requests.get(url=url, headers=header)
page = response.text
soup = BeautifulSoup(page, "lxml")

price_text = soup.find(name="span", class_="a-price-whole")
price = price_text.get_text()

price_first = price.split(".")[0]
price_second = int(price_first.replace(",", ""))

print(price_first, price_second)



