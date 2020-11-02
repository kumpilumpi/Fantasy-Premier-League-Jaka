# Poskusam iz league ID dobiti id od vseh team v tej ligi.

# https://github.com/spinach/FantasyPremierLeague.py/tree/python3
#   Git repozitorji z kodo

# spletni naslov za naš league id --> https://fantasy.premierleague.com/api/leagues-classic/746814/standings/


#---------------------Imports-----------------------

import requests
import json
import os
import sys
import csv

#---------------------Variabiles-----------------------

#jsondic ima vnose false =! False in null =! None
false = False
null = None
#zgleda da popravi težavo

#---------------------Kje sem ostal -----------------

#Imam funkcije, ki mi z League_id naredijo mapo shranijo notr json in csv z info o ligi igralci 

#v csv file piše vsakič z dodatno vrstico presledka bo problem za pandas?

#---------------------Functions-----------------------


def make_folder(ime): #dela
    'Creates folder where all csv and jsos will be located'
    if not os.path.exists(os.path.join('Data_analysis', ime)):
        os.makedirs(os.path.join('Data_analysis', ime))
    pass


def league(league_id): 
    'Returns json info about a league'
    r = requests.get(f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/")
    jsondic = r.json()
    try:
        with open(os.path.join('Data_analysis', f'league_{league_id}', f'json_mini_league{league_id}.json'), 'w') as file:     #Path? bolj elegantna rešitev #Problem ne obstoj mape
            json.dump(jsondic, file)
    except FileNotFoundError: #ker folder, še ni ustvrajen z make_folder
        pass
    return jsondic


def csv_league_info(league_id,jsondic): #problem, ker tudi če ni csv_league poklican pokliče league in javlja napako
    'Creates csv with info about mini league'
    league_v = jsondic.get('league') #to je seznam z info o ligi

    headers = list(league_v.keys())
    with open(os.path.join('Data_analysis' ,f'league_{league_id}', f'csv_mini_l_info{league_id}.csv'), 'w', encoding="utf-8") as file: #encoding ="utf-8", težave z čudnimi znaki v imenih \u0000
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerow(league_v)

    pass


def csv_players_in_league(league_id, jsondic):
    'Creates csv with info about mini league players'

    standings = jsondic.get('standings')
    results = standings.get('results') #to je seznam za vsakega igralca s potrebnimi info

    headers = list(results[0].keys())

    with open(os.path.join('Data_analysis', f'league_{league_id}', f'csv_mini_l_players{league_id}.csv'), 'w', encoding="utf-8") as file: #encoding ="utf-8", težave z čudnimi znaki v imenih \u0000
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for player in results:
            writer.writerow(player)

    pass


def main_fun(id):
    'Combines all other functions'
    league_id = str(id)

    jsondic = league(league_id)
    make_folder(f'league_{league_id}')
    csv_league_info(league_id,jsondic)
    csv_players_in_league(league_id, jsondic)

    pass

#-----------Preverjanje------------

# jsondic = League() #bi vrnila
# new_entries = jsondic.get('new_entries')
# standings = jsondic.get('standings')
# results = standings.get('results')

# print(results[1].keys())

# make_folder()
# csv_players_in_league(league())
# csv_league_info(league())


# main_fun(355255)
