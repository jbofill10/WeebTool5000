#!/usr/bin/env python3

from website_util import util
from user_settings import profile
from browser import Browser
from rich.console import Console
from multiprocessing import Process

import cli
import sys

console = Console()


def main():

    user_cnf = profile.config()

    console.print('-_-_-_- WeebTool5000 -_-_-_-'.center(50), style='bold red')
    print('\n')
    while True:
        response = input('1) Search Anime\n' +
                         '2) Watch Anime\n' +
                         '3) Settings\n' +
                         '4) Exit\n\n~> ')

        # Search anime
        if response == '1':
            anime = input('Search an anime: ')

            data = util.query_anime(anime)

            selected_anime = cli.anime_selection(data)

            cli.save_anime(selected_anime)

        # Watch Anime
        elif response == '2':

            anime = cli.pick_anime()

            brwser = Browser(user_cnf)

            brwser.watch_episode(anime['curr_ep'])

            # track browser url
            Process(target=brwser.manage_url,
                    kwargs={'ep_name': anime['name']}).start()

        # Settings
        elif response == '3':
            response = input('1) Change Name\n' +
                             '2) Edit Animes\n' +
                             '3) Reset Profile\n\n' +
                             '~> Choose a number: ')

            # Change name
            if response == '1':
                pass

            # Edit Animes
            elif response == '2':
                data = profile.get_config()
                if len(data) == 0:
                    print('No animes saved :(')
                    continue

                action = input('1) Delete\n' +
                               '2) Change Order\n' +
                               '3) Change Episode\n\n' +
                               '~> Choose a number: ')

                cli.show_animes()

                anime = input('~> Select an anime by number: ')

                key = list(data)[int(anime)-1]

                # Delete
                if action == '1':
                    del data[key]

                # Change Order
                elif action == '2':

                    to_swap = input('~> Select anime you want to swap: ')

                    keys = list(data)

                    temp = keys[int(to_swap)-1]

                    keys[int(to_swap)-1] = keys[int(anime)-1]

                    keys[int(anime)-1] = temp

                    data = type(data)((k, data[k]) for k in keys)

                    profile.save_config(data)

                # Change episode
                elif action == '3':

                    print('What episode are you on?')
                    ep = input('~> ')

                    ep = '0'+ep if ep[0] != 0 and int(ep) < 10 else ep

                    episode = util.get_episode(data[key]['slug'], ep)

                    data[key]['curr_ep'] = episode

                    profile.save_config(data)

            # Reset Profile
            elif response == '3':
                pass
            profile.save_config(data)

        # Exit
        elif response == '4':
            sys.exit(0)


if __name__ == '__main__':
    main()
