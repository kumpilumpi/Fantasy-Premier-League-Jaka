# Rad bi naredil datoteko, ki iz info, ki jih pobere league_info predvsem player_id
# Z orodji od vaastava potem pokliče team_scraper.py in jih shrani v isto mapo kot league_info

#Main file, ki združuje players_scrapper.py in league_info.py

#1. League_info ustvari folderje pobere podatke o ligi
#2. Player_scrapper ustvari še podrbne podatke za vsakega igralca v ligi
#3. Da bi vsa zadevadelovala tako, da samo v terminal vpišeš Main.py <League_id> in ti vse naredi

#------------------Import--------------------
from player_scraper import poberi_vsi, poberi

from league_info import main_fun

#--------------------------------------------

#problem z importi in relativnimi potmi
#imoprt od importa

#------------------Fun-----------------------

def main(league_id):
    poberi_vsi(league_id, main_fun(league_id))
    pass

#--------------------------------------------



# main(746814)