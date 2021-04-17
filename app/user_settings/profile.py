import os
import pickle


def config():
    if os.path.exists('user.cnf'):
        f = open('user.cnf', 'rb')

        cnf = pickle.load(f)

        print(f'\nWelcome back, {cnf["name"]}\n')

    else:
        cnf = {}
        f = open('user.cnf', 'wb')
        user_name = input('Hello weeb, what is your name: ')
        wsl = input('Are you are running this in wsl (n if you don\'t know)? (y/n):')
        wsl = True if wsl == 'y' else False
        cnf['name'] = user_name
        cnf['wsl'] = wsl

        pickle.dump(cnf, f)

    return cnf


def get_config():

    if not os.path.exists('db.pickle'):
        open('db.pickle', 'wb').close()

    return pickle.load(open('db.pickle', 'rb'))


def save_config(data):

    f = open('db.pickle', 'wb')

    pickle.dump(data, f)
