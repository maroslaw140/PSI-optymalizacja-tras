import random
import math


def koduj_genotyp(tablica, wielkosc_populacji):
    poczatkowa_populacja = []
    for _ in range(wielkosc_populacji):
        chromosom = random.sample(tablica, len(tablica))
        poczatkowa_populacja.append(chromosom)
    return poczatkowa_populacja


def selekcja_turniejowa(populacja, wyniki_oceny, rozmiar_turnieju):
    nowa_populacja = []
    for _ in range(len(populacja)):
        turniej = random.sample(list(enumerate(wyniki_oceny)), rozmiar_turnieju)
        zwyciezca_turnieju = min(turniej, key=lambda x: x[1])[0]
        nowa_populacja.append(populacja[zwyciezca_turnieju])
    return nowa_populacja


def krzyzowanie_jednopunktowe(rodzic1, rodzic2):
    punkt_podzialu = random.randint(0, len(rodzic1) - 1)
    dziecko1 = rodzic1[:punkt_podzialu] + [gen for gen in rodzic2 if gen not in rodzic1[:punkt_podzialu]]
    dziecko2 = rodzic2[:punkt_podzialu] + [gen for gen in rodzic1 if gen not in rodzic2[:punkt_podzialu]]
    return dziecko1, dziecko2


def mutacja_zmiany_miast(chromosom, prawdopodobienstwo_mutacji):
    if random.random() < prawdopodobienstwo_mutacji:
        indeks1, indeks2 = random.sample(range(len(chromosom)), 2)
        chromosom[indeks1], chromosom[indeks2] = chromosom[indeks2], chromosom[indeks1]
    return chromosom


def generuj_macierz_kosztow(klienci):
    macierz_kosztow = {}

    try:
        for klient1 in klienci.values():
            macierz_kosztow[klient1.id] = {}
            for klient2 in klienci.values():
                if klient1 != klient2:
                    koszt = pitagoras(klient1.wspolrzednaY, klient1.wspolrzednaX, klient2.wspolrzednaY,
                                      klient2.wspolrzednaX)
                    macierz_kosztow[klient1.id][klient2.id] = koszt

    except Exception as e:
        print(f"Błąd: {e}")

    return macierz_kosztow


def pitagoras(y1, x1, y2, x2):
    try:
        roznica_szerokosci = (y2 - y1) * 111
        roznica_dlugosci = (x2 - x1) * (111 * math.cos(math.radians(y1)))

        return math.sqrt(roznica_szerokosci ** 2 + roznica_dlugosci ** 2)

    except Exception as e:
        print(f"Błąd: {e}")


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
