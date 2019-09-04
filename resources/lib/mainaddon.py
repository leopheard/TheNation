import requests
import re
from bs4 import BeautifulSoup

url1 = "https://audioboom.com/channels/4993313.rss" #NEXTLEFT
url2 = "https://audioboom.com/channels/4950433.rss" #SMS
url3 = "https://audioboom.com/channels/4949998.rss" #SPORTS

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
get_soup1("https://audioboom.com/channels/4993313.rss")

def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
get_soup2("https://audioboom.com/channels/4950433.rss")

def get_soup3(url3):
    page = requests.get(url3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup3))
    return soup3
get_soup3("https://audioboom.com/channels/4949998.rss")

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://www.thenation.com/wp-content/uploads/2019/05/NextLeft-logo-final-300.png",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/79/1f/e2/791fe26e-0969-543f-2c45-6c2442a0fcba/mza_4618973306427568854.jpg/600x600wp.png",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast3(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Music122/v4/4f/3b/d3/4f3bd362-5300-a3aa-15af-01bcff709d69/source/1200x630bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
