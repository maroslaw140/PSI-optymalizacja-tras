import random

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
