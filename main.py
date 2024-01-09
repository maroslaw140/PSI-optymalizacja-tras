from classKlient import Klient
from koszt import *
from algorytm_genetyczny import *
import csv
import random
import folium

wielkosc_populacji = 100
liczba_pokolen = 1000

liczba_krzyzowan = 500
rozmiar_turnieju = 20
prawdopodobienstwo_mutacji = 0.01
liczba_elit = 100

klienci = []
oznaczenia_klientow = []

macierz_kosztow = wczytaj_macierz_kosztow('daneKoszt.csv')

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
    wyniki_oceny = [sumuj_koszt(trasa, macierz_kosztow) for trasa in populacja]

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
    wyniki_oceny_nowej_populacji = [sumuj_koszt(trasa, macierz_kosztow) for trasa in nowa_populacja]

    # Elitaryzm - wybór najlepszych rozwiązań do kolejnego pokolenia
    najlepsze_indeksy = sorted(range(len(wyniki_oceny_nowej_populacji)), key=lambda k: wyniki_oceny_nowej_populacji[k])[
                        :liczba_elit]
    nowa_populacja = [nowa_populacja[indeks] for indeks in najlepsze_indeksy]

    # Zastąpienie starej populacji nową populacją
    populacja = nowa_populacja

# Ostateczna ocena jakości najlepszego rozwiązania
wyniki_oceny = [sumuj_koszt(trasa, macierz_kosztow) for trasa in populacja]
najlepsze_rozwiazanie = populacja[wyniki_oceny.index(min(wyniki_oceny))]

# Przemapowanie oznaczeń klientów na nazwy miast
najlepsze_rozwiazanie = [klient.miasto for oznaczenie in najlepsze_rozwiazanie for klient in klienci if oznaczenie == klient.oznaczenie]

print(najlepsze_rozwiazanie)

# Tworzenie słownika miast na podstawie informacji o klientach
miasta = {}
for klient in klienci:
    miasto_klienta = klient.miasto
    wspolrzedne = [klient.wspolrzednaX, klient.wspolrzednaY]
    miasta[miasto_klienta] = wspolrzedne

# Tworzenie mapy w bibliotece Folium
mapa = folium.Map(location=[52.237049, 19.017532], zoom_start=6)

# Dodawanie znaczników na mapie dla każdego miasta
for miasto, wspolrzedne in miasta.items():
    folium.Marker(location=wspolrzedne, popup=miasto).add_to(mapa)

# Tworzenie tras na mapie
for i in range(len(najlepsze_rozwiazanie) - 1):
    start = najlepsze_rozwiazanie[i]
    end = najlepsze_rozwiazanie[i + 1]
    folium.PolyLine(locations=[miasta[start], miasta[end]], color='blue').add_to(mapa)

# Zapisanie mapy do pliku HTML
mapa.save("mapa.html")



