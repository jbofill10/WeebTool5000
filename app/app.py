#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from website_util import util
from user_settings import profile

import os, pickle, requests, json, sys


def main():
    profile.config()

    print('-_-_-_- WeebTool5000 -_-_-_-'.center(50))

    while True:
        response = input('1) Search Anime\n2) List current saved animes\n3) Settings\n4) Exit\n\n~> ')

        if response == '1':
            anime = input('Search an anime: ')
            
            data = util.query_anime(anime)

            selected_anime = anime_selection(data)

            print(selected_anime)

            save_anime(selected_anime)

        elif response == '2':
            fetch_animes()

        elif response == '3':
            pass

        elif response == '4':
            sys.exit(0)

    print('Current Animes:')
    options = Options()
    options.add_extension('extension_1_34_0_0.crx')
    global driver
    driver = webdriver.Chrome(options=options, 
            executable_path='/usr/local/lib/python3.8/dist-packages/chromedriver_py/chromedriver_win32.exe')
    
    driver.get('http://www.google.com')

def fetch_animes():
    data = {}
    if os.path.exists('db.pickle'):
        f = open('db.pickle', 'rb')

        data = pickle.load(f)

        for anime in data:
            print(anime['name'])

    else:
        f = open('db.pickle', 'wb')
        pickle.dump(data, file=f)

    if len(data) == 0:
        print('No animes saved :(')

def anime_selection(data):
    for i in range(0, len(data)-1, 2):
        print('{}) {:70s} {}) {}'.format(i+1, data[i]['name'], i+2, data[i+1]['name']))

    selection = input('~> Enter number to add anime to collection: ')

    return data[int(selection)-1]

def save_anime(anime):

    episode = util.get_episode(anime['slug'], '01')
    
    anime['curr_ep'] = episode
    
    data = []
    data.append(anime)
    f = open('db.pickle', 'wb')
    pickle.dump(data, f)




if __name__ == '__main__':
    main()
