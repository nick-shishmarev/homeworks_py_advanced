import re

import requests
import bs4

from fake_headers import Headers

# Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# Ваш код

url = 'https://habr.com'
url_tail = '/ru/articles/'

headers = Headers(browser='chrome', os='win').generate()
regex = re.compile('|'.join(f"\\b{kw}\\b" for kw in KEYWORDS), re.IGNORECASE)

response = requests.get(url+url_tail, headers=headers)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, features='lxml')

for article in soup.find_all('article', class_='tm-articles-list__item'):
    title_tag = article.find('a', class_='tm-title__link')
    article_name = title_tag.span.text
    article_link = f"{url}{title_tag['href']}"
    article_time = article.find('time')['title']

    preview_tag = article.find('div', class_='tm-article-body tm-article-snippet__lead')
    preview_txt = preview_tag.get_text(separator=' ') if preview_tag else ''

    if regex.search(preview_txt):
        print(f"{article_time}  -  {article_name}  -  {article_link}")
        continue

    response = requests.get(article_link, headers=headers)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, features='lxml')

    article_body = soup.find(
        'div',
        class_="article-formatted-body article-formatted-body article-formatted-body_version-2"
    )

    if article_body:
        article_text = article_body.find_all('p')
    else:
        article_text = []

    text = article_body.get_text(separator=' ') if article_body else ''

    if regex.search(text):
        print(f"{article_time}  -  {article_name}  -  {article_link}")
