class Koszt:
    @staticmethod
    def wczytaj_macierz_kosztow(plik):
        macierz_kosztow = []

        with open(plik, newline='') as plik_csv:
            import csv
            czytnik_csv = csv.reader(plik_csv)
            for i, linia in enumerate(czytnik_csv):
                if i > 0:  # Pomijanie pierwszego wiersza (indeks 0)
                    macierz_kosztow.append([int(element) if element.isdigit() else element for element in linia[1:]])

        return macierz_kosztow

