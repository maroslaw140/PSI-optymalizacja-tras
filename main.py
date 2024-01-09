from classKlient import Klient
from classKoszt import Koszt
from algorytm_genetyczny import *
import csv
import random

wielkosc_populacji = 100
liczba_pokolen = 100

liczba_krzyzowan = 50
rozmiar_turnieju = 2
prawdopodobienstwo_mutacji = 0.1
liczba_elit = 10

klienci = []
oznaczenia_klientow = []

macierz_kosztow = Koszt.wczytaj_macierz_kosztow('daneKoszt.csv')

with open('daneKlient.csv', newline='', encoding='utf-8') as plik_csv:
    czytnik_csv = csv.reader(plik_csv)
    for linia in czytnik_csv:
        nowy_klient = Klient()
        nowy_klient.przypisz(','.join(linia))
        klienci.append(nowy_klient)

        oznaczenia_klientow.append(nowy_klient.oznaczenie)

populacja = generuj_populacje(oznaczenia_klientow, wielkosc_populacji)

# Ewolucja populacji przez określoną liczbę pokoleń


for pokolenie in range(liczba_pokolen):
    # Ocena jakości każdego chromosomu w populacji
    wyniki_oceny = [Koszt.sumuj_koszt(trasa, macierz_kosztow) for trasa in populacja]

    # Selekcja turniejowa
    nowa_populacja = selekcja_turniejowa(populacja, wyniki_oceny, rozmiar_turnieju)

    # Krzyżowanie jednopunktowe
    for _ in range(liczba_krzyzowan):
        indeks_rodzica1, indeks_rodzica2 = random.sample(range(len(nowa_populacja)), 2)
        rodzic1, rodzic2 = nowa_populacja[indeks_rodzica1], nowa_populacja[indeks_rodzica2]
        dziecko1, dziecko2 = krzyzowanie_jednopunktowe(rodzic1, rodzic2)
        nowa_populacja.extend([dziecko1, dziecko2])

    # Mutacja zmiany miast
    for i in range(len(nowa_populacja)):
        nowa_populacja[i] = mutacja_zmiany_miast(nowa_populacja[i], prawdopodobienstwo_mutacji)

    # Ocena jakości nowej populacji
    wyniki_oceny_nowej_populacji = [Koszt.sumuj_koszt(trasa, macierz_kosztow) for trasa in nowa_populacja]

    # Elitaryzm - wybór najlepszych rozwiązań do kolejnego pokolenia
    najlepsze_indeksy = sorted(range(len(wyniki_oceny_nowej_populacji)), key=lambda k: wyniki_oceny_nowej_populacji[k])[
                        :liczba_elit]
    nowa_populacja = [nowa_populacja[indeks] for indeks in najlepsze_indeksy]

    # Zastąpienie starej populacji nową populacją
    populacja = nowa_populacja

# Ostateczna ocena jakości najlepszego rozwiązania
wyniki_oceny = [Koszt.sumuj_koszt(trasa, macierz_kosztow) for trasa in populacja]
najlepsze_rozwiazanie = populacja[wyniki_oceny.index(min(wyniki_oceny))]

print(najlepsze_rozwiazanie)
