# z vaasatv team scrapper pobere info o ekipi


#-------------------Imports-----------------
import sys
import os

sys.path.insert(0, os.path.join('FPL-vaastav')) #Omogoča, da se teams_scraper importa, ker je v drugi mapi
from teams_scraper import *


#-------------------Komentarji-----------------

#kaj pa če mape za ligo še ni

#-------------------Funkcije-----------------

def poberi(league_id, id): #namenjena da teče le znotraj poberi vse
    'Creates a folder and uses teams_scrapper on one team to dump all data in there'

    season = "20_21"
    output_folder = "team_" + str(id) + "_data" + season

    #------Sama ta funkcija dela file v napačnem folderju
    path_cd = os.path.join('Data_analysis', f'league_{league_id}') 
    os.chdir(path_cd)
    #------To popravi lokacijo, ta koda je v poberi_vse(), ki poravi težavo

    if not os.path.exists(output_folder): #ker smo šli z chdir že v league folder je kle output folder ok
        os.makedirs(output_folder) 
    store_data(id, output_folder) #ni napake -> ne zanzna importa -> popravljeno  


def poberi_vsi(league_id, list_id):
    'For each member of league runs poberi()'

    #spremeni cd drugače mkdir kr nekje naredi mapo
    path_cd = os.path.join('Data_analysis', f'league_{league_id}') 
    os.chdir(path_cd)

    for player in list_id:
        poberi(league_id, player)
    pass


#----------------------Test-----------------------------
# poberi(746814, 3952673) #dela