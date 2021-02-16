# orodja s katerimi bi pobiral dataframe in vse  skupaj shranjeval v slovarjih, treba bo veliko vnest

#-------------Imports---------------

import pandas as pd
import os 
import sys

# print (sys.path)

#-----------------------------------

# Hočem dictionary, liga =  {[ime-ekipe, id] : dataframe-vsi podatki v ekipi }
#dataframes
    # csv_mini_l_players<id>.csv -> vsi osnovni podatki (imena. id, ...)
    # GWs ->
    # En skupni dataframe, k bo vseboval vse picke/ekipe vseh GW
    # uporabljeni chipi (a ne kaže pri pickih ? )
    # vse menjave


#--------------Fun------------------

def get_dic(league_id):
    '''Creates dictionary of {id : name}'''
    gen_path = os.path.join( os.pardir, 'Data_analysis', f'league_{league_id}', f'csv_mini_l_players{league_id}.csv') # -> Probaj os.pardir dati v except
    df_general = pd.read_csv(gen_path)

    ids = df_general.entry.tolist()
    names = df_general.entry_name.tolist()
    dic_id_name ={ids[i] : names[i] for i in range(len(ids))}
    return dic_id_name


def get_list_id(league_id): 
    return list(get_dic(league_id).keys())


def gws_collect(league_id): 
    ''' Collects info about gws from each player and joins then in one dictionary {id : df} '''
    gws_pl = {}

    for (id_ , name) in get_dic(league_id).items() :
        try:
            rel_path = os.path.join(os.pardir, 'Data_analysis', f'league_{league_id}', f'team_{id_}', 'gws.csv') # os.pardir -> ker ko importam v drug file se tam poti pokvarijo, ne vem zkj
            df = pd.read_csv(rel_path)
            df["id"] = id_
            df["team_name"] = name
            gws_pl[id_] = df
        except:
            print(f"Problem with {id_} - {name}")           
            
    #Je naredil slovar id : df -> združimo vse v en df -> nardimo raj to kr v .ipnyb filu
    # df = pd.concat(list(gws_pl.values()))
    
    return gws_pl # -> Če bomo rabl bomo že v pandasih združl pol



def chips_collect(league_id):
    ''' Collects info about chips for each player in a dictionary '''
    chips_pl = {}
    for (id_ , name) in get_dic(league_id).items() :
        try:
            rel_path = os.path.join(os.pardir, 'Data_analysis', f'league_{league_id}', f'team_{id_}', 'chips.csv') # os.pardir -> ker ko importam v drug file se tam poti pokvarijo, ne vem zkj
            df = pd.read_csv(rel_path)
            df["id"] = id_
            df["team_name"] = name
            chips_pl[id_] = df
        except:
            pass
    return chips_pl


def picks_collect(league_id):
    ''' Collects info about chips for each player in a dictionary '''
    picks = {}
    
    for (id_ , name) in get_dic(league_id).items() :
        try:
            rel_path = os.path.join(os.pardir, 'Data_analysis', f'league_{league_id}', f'team_{id_}', 'chips.csv') # os.pardir -> ker ko importam v drug file se tam poti pokvarijo, ne vem zkj
            df = pd.read_csv(rel_path)
            df["id"] = id_
            df["team_name"] = name
            chips_pl[id_] = df
        except:
            pass
    return chips_pl

#-----------------------------------



#-----------------------------------
x = chips_collect(746814)

