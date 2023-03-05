from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/newest")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("a")
    print(link)
    article_links.append(link)

article_upvote = [int(score.get_text().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvote)
article = soup.find(name="span", class_="titleline")
print(article)
