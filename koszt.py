def wczytaj_macierz_kosztow(plik):
    macierz_kosztow = {}

    try:
        with open(plik, newline='') as plik_csv:
            import csv
            czytnik_csv = csv.reader(plik_csv)
            nazwy_klientow = None
            for i, linia in enumerate(czytnik_csv):
                if i == 0:
                    nazwy_klientow = linia[1:]
                    for klient in nazwy_klientow:
                        macierz_kosztow[klient] = {}
                else:
                    klient_aktualny = linia[0]
                    koszty = linia[1:]
                    for j, koszt in enumerate(koszty):
                        macierz_kosztow[klient_aktualny][nazwy_klientow[j]] = int(koszt)

    except FileNotFoundError as e:
        print(f"Błąd odczytu pliku: {e}")
    except Exception as e:
        print(f"Błąd: {e}")

    return macierz_kosztow


def sumuj_koszt(trasa, macierz_kosztow):
    koszt = 0
    try:
        for i in range(len(trasa) - 1):
            klient_aktualny = trasa[i]
            klient_nastepny = trasa[i + 1]
            koszt += macierz_kosztow[klient_aktualny][klient_nastepny]

    except KeyError as e:
        print(f"Błąd: brak klucza {e} w macierzy kosztów!")
    except Exception as e:
        print(f"Błąd: {e}")

    return koszt
