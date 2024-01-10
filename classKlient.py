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
            try:
                self.wspolrzednaX = float(wspolrzednaX)
                self.wspolrzednaY = float(wspolrzednaY)
            except ValueError:
                raise ValueError("Nieprawidłowy format współrzędnych")
        else:
            raise ValueError("Nieprawidłowy format danych")
