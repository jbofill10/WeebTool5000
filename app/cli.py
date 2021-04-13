from rich.console import Console
from rich.table import Table
from website_util import util

import pickle
import os

console = Console()


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
    table = Table(title='Saved Animes')
    table.add_column("Name", style='cyan')
    table.add_column("Current Episode", style='green')

    cnt = 1

    for k, v in data.items():
        ep = v['curr_ep']

        ep = ep[ep.rindex('/')+1:]

        ep = ep[:ep.rindex('-')].split('-')

        table.add_row(f'{cnt}) {v["name"]}', f'{ep[0].capitalize()} {ep[1]}')

        cnt += 1

    print('\n\n')

    console.print(table)

    print('\n\n')

    anime = input('~> Select an anime by number: ')

    key = list(data)[int(anime)-1]

    return data[key]


def anime_selection(data):

    for i in range(0, len(data)-1, 2):
        print('{}) {:70s} {}) {}'.format(i+1, data[i]['name'], i+2, data[i+1]['name']))

    selection = input('~> Enter number to add anime to collection: ')

    return data[int(selection)-1]


def save_anime(anime):

    episode = util.get_episode(anime['slug'], '01')

    data = dict()

    anime['curr_ep'] = episode

    if os.path.isfile('db.pickle'):
        data = pickle.load(open('db.pickle', 'rb'))

    if anime['name'] not in data:
        data[anime['name']] = anime

    else:
        print('Already have this anime saved!')

    f = open('db.pickle', 'wb')
    pickle.dump(data, f)
