# Logboek 

## week 18
Deze week hadden wij meivakantie, naast het genieten van de vakantie heb ik een beginnetje gemaakt aan mijn code ik heb de volgende dingen weten op te stellen:

### Index.html & Layout.html
Ik heb op internet zitten zoeken naar hoe je een fancy layout/homepagina kan maken. Uiteindelijk heb op meerdere filmpjes een homepagina gemaakt met veel css en deze natuurlijk gecustimized naar mijn applicatie. source: https://www.youtube.com/watch?v=FZQxPTV3cFk

### Sign.html
Ik ben in de vakantie ook opzoek gegaan naar hoe je een mooie layout kan maken bij het ontwerpen van de registratie/login pagina. Ik kwam toen een forum tegen waarin duidelijk werd uitgelegd hoe je beide kon combineren op 1 pagina. Dit zag er vet uit en heb met behulp van de stappen van het forum deze sign pagina gemaakt. Source: https://www.florin-pop.com/blog/2019/03/double-slider-sign-in-up-form/

## week 19

### 10-05-2021
Ik had de codes van de 2 pagina's in de vakantie offline gemaakt en nog niet toegevoegd aan de structuur. Ik kwam er vandaag achter dat er veel mistte in de starterscode. Dus ik heb een project aangemaakt en deze 'final' genoemd daarbij horende heb een app aangemaakt en deze 'tvwatch' genoemd. Ik heb alle mappenstructuren toegevoegd om aan de slag te gaan. Denk hierbij aan een map met templates, static. Daarnaast heb ik een begin gemaakt met de database structuren zoals het werkend maken van de login, register en logout. Ik heb de voorbeelapp genaamd 'app' verwijdert omdat ik dus een nieuwe app had aangemaakt.

### 11-05-2021
Ik heb vandaag op internet gezocht hoe ik een api kan importeren in django met behulp van dit filmpje heb ik een werekende pagina gekregen alleen is het nu gehardcode in javascript en heb nog geen indee hoe ik data moet koppelen aan javascript van models.py. Source: https://www.youtube.com/watch?v=dtKciwk_si4&t=17174s

Ik heb daarnaast een opzetje gemaakt voor mijn interest form waar de users hun interesses kunnen laten weten en daarop worden de resultaten van tvshows op gebaseerd.

### 12-05-2021
Ik heb vandaag de opzet van de interesse pagina/form afgemaakt met de bijbehorend koppeling tot de models.py database. Daarnaast heb ik een link toegevoegd in api.py waardoor je dus naar een een detail pagina gaat (deze pagina moet nog gemaakt worden). Ik heb ook heel lang gekloot met de connectie van models.py naar api.js. Dit is mij niet gelukt en zal daar volgende week weer naar kijken.

## week 20

### 17-05-2021
Ik heb vandaag de hele dag geprobeerd mijn API dynamisch te krijgen alleen is dat me dus helemaal niet gelukt, ik zit hier al best wel lang mee te puzzelen en ben op het moment het overzicht verloren van waar ik nou moet beginnen. Assistentie heeft helaas niet de tijd om mij opweg te helpen omdat het zo druk is bij de assistentie. Ik hoop dat ik er uitkom (want op dit tempo zal het niet lukken). Ik heb alvast de detail pagina opzet gemaakt, met daarin de info gehardcode. Zodra ik eruit ben hoe ik deze info kan overbrengen van mijn API zal dit dynamisch worden.


### 18-05-2021
Vandaag ben heb ik een gesprekje gehad om mijn API wereknd te krijgen met Jelle, na de sessie met Jelle heb ik veel vooruitgang gemaakt. Ik heb de API werkend gekregen in views.py dit scheelt heel veel werk om deze data te verzenden naar een html pagina. Dus dan hoef ik de API niet op te roepen in javascript. Daarnaast heb ik de reccomendation pagina werkend nadat de user inlogt en zijn interesses invult kom je op een pagina met de reccomended tvshows gebaseerd op de input van de user. alleen is dit dus tijdelijk en moet ik ervoor zorgen dat deze dat altijd aanwezig is voor een bepaalde user. Hier zal ik morgen mee aan de slag gaan en proberen de detail pagina te fixen door als je op meer info klikt je dus op een pagina komt met uitgebreidere info.

### 19-05-2021
Ik heb vandaag grote stappen gemaakt, ik heb ervoor gezorgt dat elke keer dat een user inlogt hij de gegevens opvraagt in de database en de goede reccomendations weergeeft. Deze zijn nu dus niet meer tijdelijk. Ik heb de input in mijn detail pagina variabel gemaakt en er zelfs voor gezorgt dat er per tvshow een werkende youtubetrailer heeft. (er moet wel nog wat aangepast worden kwa design). Daarnaast moet ik nog mylist maken en ervoor zorgen dat de user favoriete tvshows kan opslaan om later te bekijken.


### 20-05-2021
Vandaag heb ik een bug ontdekt die ervoor zorgde dat als er een youtubefilmpje aanwezig was de pagina niet laadde, dit heb ik opgelost. Daarnaast heb ik vandaag mijn "My List" pagina gemaakt waarop de user zijn favoriete tv-shows kan opslaan en ervoor gezorgd dat de user niet meerdere van dezelfde tv-shows in de lijst kan opslaan. Daarnaast heb ik een (extra) functie toegevoegd waardoor de user niet alleen dingen kan toevoegen aan de favorieten maar er ook tv-shows van kan verwijderen. Daarnaast heb ik de "About us" gemaakt gebaseerd op deze (source): https://www.youtube.com/watch?v=8kS1B5iaBmg

### 21-05-2021
Ik heb vandaag de hele dag gezeten om nog een grote extra functie toe te voegen en dat is dat als je de dtail pagina opent van een bepaald tv-show je onderin de pagina automatisch gegenereerde tvshows krijgt die verglijkbaar zijn met de tvshow die je nu aan het bekijken bent. Ik heb hier heel veel moeten veranderen aan mijn code om ervoor te zorgen dat je ook deze tv-shows kan inspecteren en ze in je lijst kan toevoegen en verwijderen. Daarnaast heb ik ook mijn styles bestand opgedeeld in meerdere css files voor de overzichtelijkheid.

## week 21

### 25-05-2021
Ik heb vandaag de laatste bugs eruit gehaald in de site en de layout aangepast van de detail pagina zodat deze mooi verspringt met de trailer van de Tv-show. Daarnaast heb ik de README aangepast en het DESIGN document aangepast/geupdate. Ik heb besloten de indeling van de foto's in de Doc's op te delen in schetsen en het huidige resultaat van de uiteindelijke site. Ik heb ook wat impressie foto's neergezet bij de documentatie van het technische overview zodat de gebruiker kan zien welke paden naar welke pagina's leiden. Ook heb ik een licensie toegevoegd in de root folder van de github pagina.

### 26-05-2021
Ik heb vandaag de laatste dingen aangepast aan mijn code en daarna mijn review met laura gemaakt en deze gedocumenteerd in REVIEW.md. Daarnaast heb ik ook de code van Sebastiaan gereviewd.