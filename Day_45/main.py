from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/newest")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find(name="span", class_="titleline")

print(article_tag)
