''' 
Rad bi naredil datoteko, ki iz info, ki jih pobere league_info predvsem player_id
Z orodji od vaastava potem pokliče team_scraper.py in jih shrani v isto mapo kot league_info

Main file, ki združuje players_scrapper.py in league_info.py

1. League_info ustvari folderje pobere podatke o ligi
2. Player_scrapper ustvari še podrbne podatke za vsakega igralca v ligi
3. Da bi vsa zadeva delovala tako, da samo v terminal vpišeš Main.py <League_id> in ti vse naredi
'''

#------------------Import--------------------
from sys import argv, exit

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

#Ni sprobano

if __name__ == "__main__": # prva stvar, ki se izvrši ko se pokliče fail #3
    'Runs the first thing in file'
    if len(argv) != 2: #da je ko kličeš iz terminala zraven še league id
        print("Usage: python Main.py <league_id>. Eg: python main.py 12345")
        exit(1)
    else:
        main(argv[1])


# main(746814) #Problem with 7069926, ne prenese
                # v player scraper odstrani try zanko, da vidimo kakšno napako javlja

