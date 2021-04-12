#!/usr/bin/env python3

from website_util import util
from user_settings import profile
from browser import Browser

import os
import pickle
import sys
import itertools


def main():

    user_cnf = profile.config()
    brwser = Browser(user_cnf)

    print('-_-_-_- WeebTool5000 -_-_-_-'.center(50))

    while True:
        response = input('1) Search Anime\n' +
        '2) List current saved animes\n' +
        '3) Settings\n' +
        '4) Exit\n\n~> ')

        if response == '1':
            anime = input('Search an anime: ')

            data = util.query_anime(anime)

            selected_anime = anime_selection(data)

            print(selected_anime)

            save_anime(selected_anime)

        elif response == '2':

            anime = pick_anime()

            brwser.watch_episode(anime['curr_ep'])

        elif response == '3':
            pass

        elif response == '4':
            sys.exit(0)


def pick_anime():

    if os.path.exists('db.pickle'):
        f = open('db.pickle', 'rb')

        data = pickle.load(f)

    else:
        f = open('db.pickle', 'wb')
        pickle.dump(data, file=f)
        return

    if len(data) == 0:
        print('No animes saved :(')
        return

    print('\n\n')
    
    half_len = len(data)//2

    l_1 = data[:half_len]
    l_2 = data[half_len:]

    cnt = 1
    for a, b in itertools.zip_longest(l_2, l_1):
        
        item_1 = '{}) {:70s}'.format(cnt, a['name'])
        
        if b:
            item_2 =  '{}) {}'.format(cnt+1, b['name'])
        else: item_2 = ''
        
        print(item_1 + item_2)

        cnt += 2

    print('\n\n')
    
    anime = input('~> Select an anime: ')

    return data[int(anime)-1]


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
