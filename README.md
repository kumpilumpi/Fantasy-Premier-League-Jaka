# Projektna naloga - Analiza Fantasy Premier league

Želim analizirati FPL (fantasy premier league) posamezne ekipe, mini lige in najboljše igralce. Ker je FPL  zelo popularna igra z že vzpostavljenim okoljem rednih igralcev, bi v končni fazi želel ustvariti program, ki bi ga lahko uporabljali vsi igralci FPL. Nekaj takih programov že obstaja eden izmed najbolj popularnih repozitorijev za analizo FPL je vaastav/Fantasy-Premier-League, od katerega sem tudi sam pobral določena orodja. Nisem pa še zasledil programov (vsaj ne takih zastonj), ki omogočajo analizo posamezne mini lige (lige, v kateri nastopajo le posamezne FPL ekipe).

Cilj v tej projektni nalogi je:
### 1. Analizirati resnične igralce Premier lige in njihov vpliv na Fantasy Premier league.

V datoteki Anlaiza_igralcev analiziram podatke igralcev Premier League predvsem njihov vpliv v FPL.

### 2. Analiza minilige

V datoteki miniliga_746814 pa analiziram miniligo FPL 2020/21 (League_id 746814), v kateri igramo manjša skupina prijateljev. 

.  
.  
.  
.  
.  
.  
.  
.  
.  
.  

Želim pa si še več in razširiti projekt  z čimbolj avtomatiziranimi orodji za analizo poljubne minilige. Pri končnem izdelku naj bi samo s preprostim ukazom v command line *python Main.py <League_id>* prenesel vse potrebne datoteke s interneta jih shrani in nato ustvrail še dodatno datoteko s osnovno analizo te minilige (po zgledu miniliga_746814)
 
Trenutno:
* Orodja za prenos podatkov so ustvarjena z ukazom *python Main.py <League_id>* se prenesejo podatki poljubne minilige v folder league_<league_id>
* Ni pa še povsem avtomatizirana analiza minilige
  

<hr>
Končna verzija readme    
  
# FANATSY PREMIER LEAGUE ANALYSIS

## Fantasy Premier League (FPL)
FPL is a game that casts you in the role of a Fantasy manager. You are given the task to pick a squad of real-life Premier League (PL) players who score points for your team based on their performances in their matches.

## Tactics
The FPL is online multiplayer strategic game. You need to include players in your squad that have a highest chance of producing points, but you are limited by player's price and position. There are many factors to consider when transfering player in or out, player form, team form, fixtures, price rises and falls and much more. So to make this a bit easier I am trying to make some tools to collect team data write it in easy to work with csv files and then analyse that with python pandas. FPL is played through entirety of premier league season. I will try to make these tools to be useful for every gameweek.

## SOURCES
 - https://github.com/vaastav/Fantasy-Premier-League  -> A repository with some great code for FPL analysis and weekly updates on player stats. Subrepository to my as I will use a lot of code and data collected here.
