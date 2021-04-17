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
        '2) List current saved animes\n' +
        '3) Settings\n' +
        '4) Exit\n\n~> ')

        if response == '1':
            anime = input('Search an anime: ')

            data = util.query_anime(anime)

            selected_anime = cli.anime_selection(data)

            print(selected_anime)

            cli.save_anime(selected_anime)

        elif response == '2':

            anime = cli.pick_anime()

            brwser = Browser(user_cnf)

            brwser.watch_episode(anime['curr_ep'])

            # track browser url
            Process(target=brwser.manage_url,
                    kwargs={'ep_name': anime['name']}).start()

        elif response == '3':
            pass
        elif response == '4':
            sys.exit(0)


if __name__ == '__main__':
    main()
