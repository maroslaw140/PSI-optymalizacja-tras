def wczytaj_macierz_kosztow(plik):
    macierz_kosztow = {}

    with open(plik, newline='') as plik_csv:
        import csv
        czytnik_csv = csv.reader(plik_csv)
        nazwy_klientow = None
        for i, linia in enumerate(czytnik_csv):
            if i == 0:  # Pierwszy wiersz zawiera nazwy klientów
                nazwy_klientow = linia[1:]
                for klient in nazwy_klientow:
                    macierz_kosztow[klient] = {}
            else:
                aktualny_klient = linia[0]
                koszty = linia[1:]
                for j, koszt in enumerate(koszty):
                    macierz_kosztow[aktualny_klient][nazwy_klientow[j]] = int(koszt)

    return macierz_kosztow

def sumuj_koszt(trasa, macierz_kosztow):
    koszt = 0
    for i in range(len(trasa) - 1):
        klient_biezacy = trasa[i]
        klient_nastepny = trasa[i + 1]
        koszt += macierz_kosztow[klient_biezacy][klient_nastepny]
    return koszt
