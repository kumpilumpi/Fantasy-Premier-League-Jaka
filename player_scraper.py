# z vaastav team scrapper pobere info o ekipi


#-------------------Imports-----------------
import sys
import os

sys.path.insert(0, os.path.join('FPL-vaastav')) #Omogoča, da se teams_scraper importa, ker je v drugi mapi

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from teams_scraper import * #napaka, prej je ni bilo?????


#-------------------Komentarji-----------------

#kaj pa če mape za ligo še ni

#Neki file od vaastava majo mogoče ugrajeno notr, časovn terminate če pedolg časa ne prenese file. Vsake tok časa kšnga entrya ne prenese

#Problem league_id ni entry id, kar v bistvu rabimmo za teams scrapper ----> Popravljeno

#-------------------Funkcije-----------------

def poberi(league_id, id): #namenjena da teče le znotraj poberi vse
    'Creates a folder and uses teams_scrapper on one team to dump all data in there'

    output_folder = "team_" + str(id)

    #------Sama ta funkcija dela file v napačnem folderju
    # path_cd = os.path.join('Data_analysis', f'league_{league_id}') 
    # os.chdir(path_cd)
    #------To popravi lokacijo, ta koda je v poberi_vse(), ki popravi težavo

    if not os.path.exists(output_folder): #ker smo šli z chdir že v league folder je kle output folder ok
        os.mkdir(output_folder) 
    store_data(id, output_folder) #ni napake -> ne zanzna importa -> popravljeno 
    

def poberi_vsi(league_id, list_entry): # Za eno zgleda vredu več funkcij povzroča napako
    'For each member of league runs poberi()'

    #spremeni cd drugače mkdir kr nekje naredi mapo
    path_cd = os.path.join('Data_analysis', f'league_{league_id}') 
    os.chdir(path_cd)

    for player_id in list_entry:
        try: 
            #ustvarja mape nč ne da v njih
            #store_data zgleda problem
            poberi(league_id, int(player_id))
        except: # ------------------------------------------------------> ne vem keatero napako javlja, probaj brez polaufati vse
            print(f'Problem with {player_id}')
    pass


#----------------------Test-----------------------------
# poberi(746814, 3952673)
# poberi_vsi(746814, [3952673, 5090020, 3327253, 1093759, 4999866, 5687292, 1025697, 3994802, 1457623, 4900127, 1841136, 5209323, 5039919, 7069926]) #pobralo vse razen ene