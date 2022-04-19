import requests
from bs4 import BeautifulSoup
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

base_url = 'https://habr.com'
url = base_url + '/ru/all/'
ret = requests.get(url, headers=HEADERS)
text = ret.text
soup = BeautifulSoup(text, features='html.parser')

posts = soup.find_all('article')
only = []

for post in posts:
    hubs = post.find_all(class_='tm-article-snippet__hubs-item')
    hubs = [hub.text.strip() for hub in hubs]
    titles = post.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('span').text
    title = titles.split()
    body_posts_1 = str(post.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-1'))
    body_posts_2 = str(post.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2'))

    for keyword in KEYWORDS:
        if re.findall(keyword, body_posts_1) or re.findall(keyword, body_posts_2):
            href = post.find(class_='tm-article-snippet__title-link').attrs['href']
            link = base_url + href
            only.append(titles)
            data_post = post.find('time').attrs['title']
            print(f'<{data_post[:10]}> - <{titles}> - <{link}>')

    for hub in hubs:
        if hub in KEYWORDS and titles not in only:
            href = post.find(class_='tm-article-snippet__title-link').attrs['href']
            link = base_url + href
            only.append(titles)
            data_post = post.find('time').attrs['title']
            print(f'<{data_post[:10]}> - <{titles}> - <{link}>')

    for tt in title:
        if tt in KEYWORDS and titles not in only:
            href = post.find(class_='tm-article-snippet__title-link').attrs['href']
            link = base_url + href
            only.append(titles)
            data_post = post.find('time').attrs['title']
            print(f'<{data_post[:10]}> - <{titles}> - <{link}>')
