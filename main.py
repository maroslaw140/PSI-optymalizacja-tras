from classKlient import Klient
from classKoszt import Koszt
import csv

klienci = []

with open('daneKlient.csv', newline='', encoding='utf-8') as plik_csv:
    czytnik_csv = csv.reader(plik_csv)
    for linia in czytnik_csv:
        nowy_klient = Klient()
        nowy_klient.przypisz(','.join(linia))
        klienci.append(nowy_klient)

for klient in klienci:
    print(f"Oznaczenie: {klient.oznaczenie}, Miasto: {klient.miasto}, Współrzędne: ({klient.wspolrzednaX}, {klient.wspolrzednaY})")

liczbaKlientow = len(klienci)


# Przykładowe użycie metody statycznej
nazwa_pliku = 'daneKoszt.csv'  # Zastąp 'twoj_plik.csv' właściwą nazwą pliku
macierz = Koszt.wczytaj_macierz_kosztow(nazwa_pliku)
print(macierz)