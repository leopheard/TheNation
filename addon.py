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
            'thumbnail': "https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fis1-ssl.mzstatic.com%2Fimage%2Fthumb%2FMusic128%2Fv4%2F6d%2F22%2Fdf%2F6d22dfe0-eb51-0737-9ebb-6a8e5ff3b02d%2Fsource%2F1200x630bb.jpg&f=1"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Music122/v4/4f/3b/d3/4f3bd362-5300-a3aa-15af-01bcff709d69/source/1200x630bb.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
