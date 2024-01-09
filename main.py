from classAlgorytmGenetyczny import AlgorytmGenetyczny
from classKlient import Klient
from classKoszt import Koszt
import csv
import random

klienci = []
oznaczenia_klientow = []

with open('daneKlient.csv', newline='', encoding='utf-8') as plik_csv:
    czytnik_csv = csv.reader(plik_csv)
    for linia in czytnik_csv:
        nowy_klient = Klient()
        nowy_klient.przypisz(','.join(linia))
        klienci.append(nowy_klient)

        oznaczenia_klientow.append(nowy_klient.oznaczenie)

liczba_klientow = len(klienci)
macierz_kosztow = Koszt.wczytaj_macierz_kosztow('daneKoszt.csv')
wielkosc_populacji = liczba_klientow ** 2

def kodowanie_genotypu():
    random.shuffle(oznaczenia_klientow)
    return oznaczenia_klientow.copy()

poczatkowa_populacja = AlgorytmGenetyczny.kodowanie_genotypu(oznaczenia_klientow)

