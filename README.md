# FANATSY PREMIER LEAGUE ANALYSIS
Zadnja točka opis za projektno nalogo.

## FPL
Fantasy Premier League is a game that casts you in the role of a Fantasy manager. You are given the task to pick a squad of real-life players who score points for your team based on their performances in their own matches.

## ANALYSIS
The FPL is complicated and strategic game. You need to include players in your squad taht have a highest chance of producing points, but you are limited by player prices and positions. There are many factors to consider whrn transfering plyer in or out player and team form, fixtures, price rises and falls and much more. So to make this a bit easier I am trying to make some tools to collect team data write it in easy to work with csv files and then analyse that with python. FPL is played through entirety of premier league season. And i am trying to make these tools be useful for every gameweek.

### TOP MANAGERS
My first analysis will be about some top managers from previus years. I hope I can find some common factors between them that I can then apply to my managerial skills.

### MINI LEAGUE
The second task is about tools that will enable analysing mini lagues. These are smaller leagues in which you are compiting with your friends. Also here would I analyse teams participating and try to find some inforamtion on how to win.

## SOURCES
 - https://github.com/vaastav/Fantasy-Premier-League  -> A repository with some great code for FPL analysis and weekly updates on player stats. Subrepository to my as I will use a lot of code and data collected here.


## Projektna naloga
Želim analizirati FPL (fantasy premier league) posamezne posmaezne ekipe, mini lige in najboljše igralce. Ker je FPL  zelo popularna igra z že vzpostavljeno družbo igralcev, bi v končni fazi želel ustvariti program, ki bi ga lahko uporabljali vsi igralci FPL. Nekaj takih programov že obstaja eden izmed najbolj popularnih repozitorijev za analizo FPL je vaastav/Fantasy-Premier-League, od katerega sem tudi sam pobral določene zadeve. Nisem pa še zasledil programov (vsaj ne takih zastonj), ki omogočajo analizo posamezne mini lige (lige, v kateri nastopajo le posamezne FPL ekipe).

Cilj je v tej projektni nalogi ustvariti:
1. Program, ki pobere podatke o ekipah vseh udeležencev mini league
2. In narediti analizo podatkov določene mini lige
Želja je da bi vse to bilo narejeno čim bolj avtomatizirano. Samo z ukazom v comand line python Main.py <league_id> ustvari mapo z vsemi csv podatki o ekipah in s pandasi naredi analizo teh mini lig (najbolj popularni igralci na Gameweek, najbolj popularni kapetani, ...).

Trenutna situacija:
Orodja za pobiranje podatkov so ustvarjena, z ukazom v command line python Main.py <league_id> naredi mapo League_<league_id> v mapi Data_analysis s vsemi pobranimi podatki.
Sam sem napisal programe, ki z league_id poberejo vse podatke o članih mini lige z orodji vaastava pa sem nato z vsemi idiji ekip pobral podrobne informacije o ekipah.
