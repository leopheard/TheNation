from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

url1 = "https://audioboom.com/channels/4993313.rss" #NEXTLEFT
url2 = "https://audioboom.com/channels/4950433.rss" #SMS
url3 = "https://audioboom.com/channels/4949998.rss" #SPORTS

#https://www.thenation.com//images/touch-icon-152x152.png

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://www.thenation.com/wp-content/uploads/2019/05/NextLeft-logo-final-300.png"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/79/1f/e2/791fe26e-0969-543f-2c45-6c2442a0fcba/mza_4618973306427568854.jpg/600x600wp.png"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Music122/v4/4f/3b/d3/4f3bd362-5300-a3aa-15af-01bcff709d69/source/1200x630bb.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup = mainaddon.get_soup(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
