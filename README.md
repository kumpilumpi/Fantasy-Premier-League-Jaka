# Projektna naloga - Analiza Fantasy Premier league

## Fantasy Premier League
Fantasy Premier League (FPL) je online taktična igra, v kateri se preizkusiš kot manager svoje sanjske Premier League ekipe. Z omejenimi sredstvi si izbereš svojo ekipo resničnih igralcev, ki ti na podlagi njihovih dosežkov v vsakem krogu prinašajo točke. Igra zahteva precej taktike in analize statistike. Za podrobnejša navodila obišči : https://fantasy.premierleague.com/help/rules

V tej projektni nalogi bom analiziral podatke Fantasy premier League (FPL). Cilj je analizirati igralce trenutne sezone in ustvariti orodja za analizo poljubne minilige (manjši izbor ekip, ki tekmuje med sabo).

## Prenos in urejanje podatkov
Za prenos podatkov sem se naslonil že na izdelan repozitorij vaastav/Fantasy-Premier-League (glej vire) in uporabil nekaj danih orodji za prenos podatkov ekip. Žal pa dan repozitorij ne ponuja možnosti prenosa podatkov o miniligi, ampak le posamezne igralce. 

* Datoteka *League_info.py* poskrbi za prenos podatkov o miniligi. Ustvari mapo league_<*league_id*>, vanjo shrani json vseh podatkov o ligi (imena ekip, idji ekip, kdaj je bila liga ustvarjena,...) in ga nato preoblikuje v uporaben csv.
* Nato datoteka player_scraper.py s pomočjo vaastav/Fantasy-Premier-League repozitorija pobere podatke o vsakem igralcu iz dane minilige. 
* Datoteka main pa združuje obe datoteki in omogoča njuno izvršitev z ukazom iz terminala *python Main.py <League_id>*.

## Analiza podatkov

Analiziral bom dva sklopa podatkov:

### 1. Resnične igralce Premier lige in njihov vpliv na Fantasy Premier league.

V datoteki Data_analysis/Analiza_igralcev analiziram podatke igralcev Premier League predvsem njihov vpliv v FPL. Poskušam odkriti kako si najbolj učinkovito razporediti sredstva po pozicijah in ali obstaja kakšna korelacija med danimi točkami igralca in kako drugo statistično kategorijo.

### 2. Minilige

V datoteki Data_analysis/miniliga pa so zbrana orodja za analizo poljubne minilige. Prvotno je analizirana miniliga v kateri igram sam s prijatelji z zelo preprosto spremembo (samo zamenajmo 8 številk, glej uporaba) pa lahko analiziramo poljubno miniligo. Ker se minilige razlikujejo precej druga od druga (število igralcev, uspešnost,...) se ne trudim s poglobljeno analizo, ampak poskrbim predvsem za uvoz in ureditev podatkov.

## Uporaba

Želja je, da bi dan repozitorij pomagal še kakšnemu FPL mangerju osvojiti miniligo.
* Če želite analizirati svojo miniligo prvo poiščite *League_id* za svojo lastno ligo. Obiščite FPL spletno stran (ne aplikacije), pojdite v svojo ligo, poglejte url, ki bi moral izgledati https://fantasy.premierleague.com/api/leagues-classic/**League_id**/standings/ -> kjer piše League_id bo v vašem urlju večmestna številka to je vaš league_id.
* Odprite terminal (poweeshell) se premaknite (cd) do tam kjer imate shranjen dan repozitorij in nato vpišite *python* <*league_id*>. Nato bi se vam morale vse potrebne datoteke prenesti (postopek lahko malo traja dobro minuto).
* V Data_analysis se vam mora pojaviti dodatna mapa Legue_<*League_id*> in v njej podmape team_<*Player_id*>, kjer so v vsaki mapi shranjeni podtaki enega igralca iz vaše lige.
* Odprite datoteko Miniliga in sledita danim navodilom v tej datoteki. Potrebno bo le še enkrat vnesti id vaše lige.

## Viri
 - https://github.com/vaastav/Fantasy-Premier-League  -> A repository with some great code for FPL analysis and weekly updates on player stats. Subrepository to my as I will use a lot of code and data collected here.
