class Klient:
    def __init__(self):
        self.oznaczenie = ""
        self.miasto = ""
        self.wspolrzednaX = 0.0
        self.wspolrzednaY = 0.0

    def przypisz(self, linia):
        dane = linia.strip().split(',')
        if len(dane) == 4:
            self.oznaczenie, self.miasto, wspolrzednaX, wspolrzednaY = dane
            self.wspolrzednaX = float(wspolrzednaX)
            self.wspolrzednaY = float(wspolrzednaY)
        else:
            raise ValueError("Nieprawidłowy format danych")