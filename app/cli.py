from rich.console import Console
from rich.table import Table
from website_util import util
from user_settings import profile

console = Console()


def pick_anime():

    data = profile.get_config()

    if len(data) == 0:
        print('No animes saved :(')
        return

    show_animes()

    anime = input('~> Select an anime by number: ')

    key = list(data)[int(anime)-1]

    return data[key]


def anime_selection(data):

    for i in range(0, len(data)-1, 2):
        print('{}) {:70s} {}) {}'.format(i+1, data[i]['name'],
                                         i+2, data[i+1]['name']))

    selection = input('~> Enter number to add anime to collection: ')

    return data[int(selection)-1]


def save_anime(anime):
    print(anime)
    res = input(f'Have you already started watching {anime["name"]}? [y/N]: ')

    if res == 'y':

        print('What episode are you on?')

        ep = input('~> ')

        ep = '0'+ep if ep[0] != 0 and int(ep) < 10 else ep

        episode = util.get_episode(anime['slug'], ep)

    else:

        episode = util.get_episode(anime['slug'], '01')

    anime['curr_ep'] = episode

    data = profile.get_config()

    if anime['name'] not in data:

        data[anime['name']] = anime

    else:

        print('Already have this anime saved!')

    profile.save_config(data)


def update_ep(ep_name, ep):

    data = profile.get_config()

    data[ep_name]['curr_ep'] = ep

    profile.save_config(data)


def show_animes():

    table = Table(title='Saved Animes')
    table.add_column("Name", style='cyan')
    table.add_column("Current Episode", style='green')

    cnt = 1

    data = profile.get_config()

    for k, v in data.items():
        ep = v['curr_ep']

        ep = ep[ep.rindex('/')+1:]

        ep = ep[:ep.rindex('-')].split('-')

        table.add_row(f'{cnt}) {v["name"]}', f'{ep[0].capitalize()} {ep[1]}')

        cnt += 1

    print('\n\n')

    console.print(table)

    print('\n\n')
