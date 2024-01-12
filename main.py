from algorytm_genetyczny import *
from classKlient import Klient
import csv
import random
import folium

wielkosc_populacji = 1000

liczba_pokolen = 1000
liczba_krzyzowan = 100
rozmiar_turnieju = 5
prawdopodobienstwo_mutacji = 0.2
liczba_elit = 150

# Warunki zatrzymania
liczba_pokolen_bez_poprawy = 50
poprzedni_najlepszy_wynik = float('inf')
pokolenie_bez_poprawy = 0

klienci = {}

with open('daneKlient.csv', newline='', encoding='utf-8') as plik_csv:
    czytnik_csv = csv.reader(plik_csv)
    for linia in czytnik_csv:
        nowy_klient = Klient()
        nowy_klient.przypisz(','.join(linia))
        klienci[nowy_klient.id] = nowy_klient

macierz_kosztow = generuj_macierz_kosztow(klienci)

populacja = koduj_genotyp(list(klienci.keys()), wielkosc_populacji)

for pokolenie in range(liczba_pokolen):
    wyniki_oceny = [sumuj_koszt(trasa, macierz_kosztow) for trasa in populacja]

    # Selekcja turniejowa   
    nowa_populacja = selekcja_turniejowa(populacja, wyniki_oceny, rozmiar_turnieju)

    # Krzyżowanie jednopunktowe
    for _ in range(liczba_krzyzowan):
        indeks_rodzica1, indeks_rodzica2 = random.sample(range(len(nowa_populacja)), 2)
        rodzic1, rodzic2 = nowa_populacja[indeks_rodzica1], nowa_populacja[indeks_rodzica2]
        dziecko1, dziecko2 = krzyzowanie_jednopunktowe(rodzic1, rodzic2)
        nowa_populacja.extend([dziecko1, dziecko2])

    # Mutacja
    for i in range(len(nowa_populacja)):
        nowa_populacja[i] = mutacja_zmiany_miast(nowa_populacja[i], prawdopodobienstwo_mutacji)

    wyniki_nowej_populacji = [sumuj_koszt(trasa, macierz_kosztow) for trasa in nowa_populacja]

    # Elitaryzm
    indeksy_wynikow = range(len(wyniki_nowej_populacji))
    posortowane_indeksy = sorted(indeksy_wynikow, key=lambda k: wyniki_nowej_populacji[k])
    najlepsze_indeksy = posortowane_indeksy[:liczba_elit]

    nowa_populacja = [nowa_populacja[indeks] for indeks in najlepsze_indeksy]

    populacja = nowa_populacja

    najlepszy_wynik = min(wyniki_oceny)
    if najlepszy_wynik >= poprzedni_najlepszy_wynik:
        pokolenie_bez_poprawy += 1
    else:
        pokolenie_bez_poprawy = 0
    poprzedni_najlepszy_wynik = najlepszy_wynik

    if pokolenie_bez_poprawy >= liczba_pokolen_bez_poprawy:
        break


wyniki_oceny = [sumuj_koszt(trasa, macierz_kosztow) for trasa in populacja]
najlepsze_rozwiazanie = populacja[wyniki_oceny.index(min(wyniki_oceny))]

najlepsze_rozwiazanie = [
    klienci[oznaczenie].nazwa
    for oznaczenie in najlepsze_rozwiazanie
]
print(najlepsze_rozwiazanie)

# Mapa
miasta = {}
for klient in klienci.values():
    miasto_klienta = klient.nazwa
    wspolrzedne = [klient.wspolrzednaX, klient.wspolrzednaY]
    miasta[miasto_klienta] = wspolrzedne

mapa = folium.Map(location=[50.6721, 17.9253], zoom_start=8)
kolor = 'darkblue'

for miasto, wspolrzedne in miasta.items():
    folium.Marker(location=wspolrzedne, popup=miasto, icon=folium.Icon(color=kolor)).add_to(mapa)

for i in range(len(najlepsze_rozwiazanie) - 1):
    poczatkowe = najlepsze_rozwiazanie[i]
    docelowe = najlepsze_rozwiazanie[i + 1]
    folium.PolyLine(locations=[miasta[poczatkowe], miasta[docelowe]], color=kolor).add_to(mapa)

mapa.save("mapa.html")
