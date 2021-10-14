import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
site = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(site.text, features='html.parser')

articles = soup.find_all('article')


links = [f"https://habr.com{article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').a['href']}"
         for article in articles]

result_articles = {}

for link in links:
    site = requests.get(link)
    soup = BeautifulSoup(site.text, features='html.parser')
    text = soup.find(class_="article-formatted-body article-formatted-body_version-2")
    if text is None:
        text = soup.find(class_="article-formatted-body article-formatted-body_version-1")
    text_for_search = text.get_text()

    for word in KEYWORDS:
        if word in text_for_search:
            date = soup.time['title']
            title = soup.title.text
            result_articles[title] = [date, link]

for articles in result_articles.items():
    print(articles[1][0], articles[0], articles[1][1])
