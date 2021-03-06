from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

hn = 'https://thehackernews.com/'
silicon = 'https://www.siliconvalley.com/'
rg = 'https://hackspace.raspberrypi.com/'

hn_list = []


def get_hn():
    r = requests.get(hn).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('div', class_='body-post clear')
    for post in posts:
        title = post.find('h2', class_='home-title').text
        url = post.find('a').get('href')
        data = {'title': title,
                'url': url}
        hn_list.append(data)


get_hn()

silicon_list = []


def get_silicon():
    r = requests.get(silicon).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('div', class_='article-info')
    for post in posts:
        title = post.find('a', class_='article-title').text
        url = post.find('a', class_='article-title').get('href')
        data = {'title': title,
                'url': url}
        silicon_list.append(data)


get_silicon()


def home(requests):
    context = {
        'hn_list': hn_list,
        'silicon_list': silicon_list,
    }
    return render(requests, 'news_app/home.html', context)
