import random

class AlgorytmGenetyczny:
    @staticmethod
    def kodowanie_genotypu(oznaczenia_klientow):
        random.shuffle(oznaczenia_klientow)
        return oznaczenia_klientow.copy()
