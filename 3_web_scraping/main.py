import re

import requests
import bs4

from fake_headers import Headers

# Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# Ваш код
regex = '|'.join(KEYWORDS)

url = 'https://habr.com'
url_tail = '/ru/articles/'

response = requests.get(url+url_tail, headers=Headers(browser='chrome', os='win').generate())

soup = bs4.BeautifulSoup(response.text, features='lxml')

article_list = soup.find_all('article', class_='tm-articles-list__item')

for article in article_list:
    article_time = article.find('time')['title']
    article_name = article.find('a', class_='tm-title__link').span.text
    article_link = f"{url}{article.find('a', class_='tm-title__link')['href']}"
    article_preview = article.find('div', class_='tm-article-body tm-article-snippet__lead')

    if article_preview:
        text = ' '.join(c.text.strip() for c in article_preview)

        if re.findall(regex, text, re.I):
            print(f"{article_time}  -  {article_name}  -  {article_link}")
            continue

    response = requests.get(article_link, headers=Headers(browser='chrome', os='win').generate())
    soup = bs4.BeautifulSoup(response.text, features='lxml')

    article_body = soup.find(
        'div',
        class_="article-formatted-body article-formatted-body article-formatted-body_version-2"
    )

    if article_body:
        article_text = article_body.find_all('p')
    else:
        article_text = []

    text = ' '.join(c.text.strip() for c in article_text)

    if re.findall(regex, text, re.I):
        print(f"{article_time}  -  {article_name}  -  {article_link}")

