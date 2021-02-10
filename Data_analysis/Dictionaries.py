# orodja s katerimi bi pobiral dataframe in vse  skupa shranjeval v slovarjih, treba bo veliko vnest

#-------------Imports---------------

import pandas as pd
from os import path

#-----------------------------------

#--------------Fun------------------

list_id = []

def chips_collect():
    ''' Collects info about chips for each player in a dictionary '''
    chips_pl = {}
    for id in list_id:
        rel_path = path.join('Data_analysis', f'league_{league_id}', f'team_{id}', 'chips.csv') # ------------------> ? Zkj data_analysis ?????
        chips_pl[f'chips_{id}'] = pd.read_csv(rel_path) # dela
    return chips_pl

def gws_collect(league_id, list_id):
    ''' Collects info about gws for each player in a dictionary'''
    gws_pl = {}
    for id in list_id:
        rel_path = path.join('Data_analysis', f'league_{league_id}', f'team_{id}', 'gws.csv') # ------------------> ? Zkj data_analysis ?????
        gws_pl[f'chips_{id}'] = pd.read_csv(rel_path) # dela
    return gws_pl

#-----------------------------------

# x = chips_collect(746814, [1025697])