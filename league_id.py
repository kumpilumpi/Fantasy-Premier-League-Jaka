# Poskusam iz league ID dobiti id od vseh team v tej ligi.

# https://github.com/spinach/FantasyPremierLeague.py/tree/python3
#   Git repozitorji z kodo

# spletni naslov za naš league id --> https://fantasy.premierleague.com/api/leagues-classic/746814746814/standings/


#---------------------Imports-----------------------

import requests
import json
import os
import sys
import csv

#---------------------Variabiles-----------------------

LEAGUE_ID = str(746814)

league_web = f"https://fantasy.premierleague.com/api/leagues-classic/{LEAGUE_ID}/standings/" #dela
folder = f'league_{LEAGUE_ID}'

#jsondic ima vnose false =/ False in null =/ None
false = False
null = None
#zgleda da popravi težavo

#---------------------Kje sem ostal -----------------

#Imam funkcije, ki mi z League_id naredijo mapo shranijo notr json in csv z info o ligi igralci 

#Rad bi pobral in shranil še info o mini league

#v csv file piše vsakič z dodatno vrstico presledka bo problem za pandas?

#---------------------Functions-----------------------

def make_folder(ime = folder): #dela
    'Creates folder where all csv and jsos will be located'
    if not os.path.exists(os.path.join('My_stats', ime)):
        os.makedirs(os.path.join('My_stats', ime))
    pass
    

def league(file_path = f'json_mini_league{LEAGUE_ID}.json', web_adress = league_web): #dela
    'Returns json info about a league'
    r = requests.get(web_adress)
    jsondic = r.json() 
    with open(os.path.join('My_stats', folder, file_path), 'w') as file:     #Path? bolj elegantna rešitev
        json.dump(jsondic, file)
    return jsondic


# def League_id():
#     'Returns list of ids from every participant in league'
#     pass


def csv_league_info(jsondic=league()):
    'Creates csv with info about mini league'
    league_v = jsondic.get('league') #to je seznam z info o ligi

    headers = list(league_v.keys())
    with open(os.path.join('My_stats', folder, f'csv_mini_l_info{LEAGUE_ID}.csv'), 'w', encoding="utf-8") as file: #encoding ="utf-8", težave z čudnimi znaki v imenih \u0000
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerow(league_v)

    pass


def csv_players_in_league(jsondic=league()):
    'Creates csv with info about mini league players'
    
    standings = jsondic.get('standings')
    results = standings.get('results') #to je seznam za vsakega igralca s potrebnimi info

    headers = list(results[0].keys())

    with open(os.path.join('My_stats', folder, f'csv_mini_l_players{LEAGUE_ID}.csv'), 'w', encoding="utf-8") as file: #encoding ="utf-8", težave z čudnimi znaki v imenih \u0000
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for player in results:
            writer.writerow(player)

    pass


#-----------Preverjanje------------

# jsondic = League() #bi vrnila
# new_entries = jsondic.get('new_entries')
# standings = jsondic.get('standings')
# results = standings.get('results')

# print(results[1].keys())

# # make_folder()
# csv_players_in_league(league())
# csv_league_info(league())

