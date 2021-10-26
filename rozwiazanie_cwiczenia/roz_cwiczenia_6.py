import datetime

dzis=datetime.date.today()
d=dzis.timetuple()
aktualny_rok = d.tm_year


podaj_imie = input('Podaj swoje imię: ')
podaj_rok = input('Podaj rok urodzenia:  ')
suma_roku = aktualny_rok - podaj_rok


print(str(podaj_imie) + ', ' + ' masz ' + str(suma_roku) + ' lat')














