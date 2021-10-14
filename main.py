import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
site = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(site.text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    article_body = article.find(class_="article-formatted-body article-formatted-body_version-2")
    if article_body is None:
        article_body = article.find(class_="article-formatted-body article-formatted-body_version-1")
    for word in KEYWORDS:
        if word in str(article_body):
            date = article.find(class_='tm-article-snippet__datetime-published').time['title']
            title = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').span.text
            link = f"https://habr.com" \
                   f"{article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').a['href']}"
            print(date, title, link)
