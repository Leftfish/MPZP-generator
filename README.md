# MPZP-generator

Narzędzie ułatwiające mieszkańcom i mieszkankom Krakowa składanie uwag do projektu miejscowego planu zagospodarowania przestrzennego. Przygotowane z myślą o planie zagospodarowania dla okolic Kobierzyńskiej.

Ponieważ to mój pierwszy w życiu kontakt z frameworkiem Flask, a na przygotowanie miałem raptem kilka godzin, aplikacja jest toporna do bólu i np. zamiast pobierać uwagi do projektu z jakiejś bazy (i zachowaćpozory uniwersalności), wszystko ma bezczelnie wrzucone do kodu. 

Ale działa...

Dostępne [na Heroku](https://generator-uwag-mpzp.herokuapp.com/).

# Uruchom lokalnie

Polecam pythona 3 ze względu na wsparcie ASCII dla polskich znaków. 

- `pip install -r requirements.txt`
- `flask run`