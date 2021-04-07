#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, pickle, requests, json, sys

def main():
    print('-_-_-_- WebTool5000 -_-_-_-'.center(50))

    while True:
        response = input('1) Search Anime\n2) List current saved animes\n3) Settings\n4) Exit\n\n~> ')

        if response == '1':
            anime = input('Search an anime: ')
                
            data = query_anime(anime)

            anime_selection(data)

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
    if os.path.exists('db.txt'):
        f = open('db.pickle', 'rb')

        data = pickle.loads(f)
    else:
        pickle.dumps(data)

    if len(data) == 0:
        print('No animes saved :(')

def query_anime(name):
    
    res = requests.get(f'https://www2.kickassanime.rs/search?q={name}').text
    
    res = res[res.index('[{'):res.index('}]')+2]
    
    data = json.loads(res)
    
    return data

def anime_selection(data):
    for anime in data:
        print(anime['name'])

if __name__ == '__main__':
    main()
