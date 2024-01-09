# PSI-optymalizacja-tras
Optymalizacja trasy dostaw za pomocą algorytmu genetycznego

Twoim zadaniem jest zastosowanie algorytmu genetycznego w celu optymalizacji trasy dostaw dla przedsiębiorstwa kurierskiego. Przedsiębiorstwo posiada zestaw klientów, którzy mają określone lokalizacje oraz pakunki do dostarczenia. Celem jest znalezienie optymalnej trasy, która minimalizuje łączny koszt lub czas dostawy.

Założenia:
1.	Przyjmij, że firma kurierska ma 10 klientów, oznaczonych jako K1, K2, ..., K10. Każdy klient ma przypisaną lokalizację, którą można przedstawić jako współrzędne geograficzne (np. szerokość i długość geograficzną).
2.	Przypisz koszt lub czas dostawy dla każdej pary klientów. Na przykład, jeśli masz dane kosztu podróży między klientami w postaci macierzy kosztów, gdzie wartość w komórce (i, j) reprezentuje koszt podróży od klienta i do klienta j, możesz utworzyć taką macierz kosztów dla wszystkich par klientów.

Kroki do wykonania:
1.	Zdefiniuj kodowanie: Stwórz odpowiednie kodowanie genotypu, które reprezentuje trasę dostaw jako sekwencję odwiedzanych klientów. Możesz wybrać kodowanie permutacyjne, w którym każdy gen odpowiada innemu klientowi.
2.	Inicjalizacja populacji: Wygeneruj początkową populację chromosomów, reprezentujących różne trasy dostaw. Populacja powinna zawierać losowo wygenerowane trasy. Przykładowo wygeneruj początkową populację chromosomów, które reprezentują różne trasy dostaw. Na przykład, możesz wygenerować 100 chromosomów, z których każdy jest permutacją K1, K2, ..., K10.
3.	Ocena funkcji celu: Zaimplementuj funkcję celu, która ocenia jakość trasy dostaw. Może to być łączny koszt dostawy, czas podróży, zużycie paliwa itp. Ocena powinna być przypisana każdemu chromosomowi w populacji. Przykładowo funkcja celu może sumować koszty podróży między klientami na trasie.
4.	Operatory genetyczne: Zdefiniuj operatory genetyczne, takie jak selekcja, krzyżowanie i mutacja, które będą stosowane na populacji w celu tworzenia nowych pokoleń. Możesz użyć popularnych technik, takich jak selekcja turniejowa, krzyżowanie jednopunktowe lub wielopunktowe oraz mutacja zmiany miasta.
5.	Proces ewolucji: Wykonuj proces ewolucji, w którym kolejne pokolenia populacji są generowane poprzez zastosowanie operacji genetycznych. Następnie oceniaj jakość każdego nowego pokolenia i ewentualnie stosuj strategie elitaryzmu, aby zachować najlepsze rozwiązania.
6.	Warunki zatrzymania: Zdefiniuj warunki zatrzymania algorytmu genetycznego. Może to być maksymalna liczba generacji, osiągnięcie satysfakcjonującego rozwiązania lub brak znaczącej poprawy przez określoną liczbę pokoleń.
7.	Prezentacja wyników: Po zakończeniu algorytmu genetycznego, przedstaw optymalną trasę dostaw, która minimalizuje koszt lub czas podróży. Możesz również wizualizować trasę na mapie dla lepszej prezentacji.
8.	Optymalizacja i eksperymenty: możesz przeprowadzić eksperymenty z różnymi parametrami algorytmu genetycznego, takimi jak rozmiar populacji, współczynnik krzyżowania i mutacji, aby znaleźć optymalne ustawienia dla danego problemu.
9.	Dokumentacja: Przygotuj dokumentację, która opisuje proces optymalizacji, użyte operatory genetyczne, wyniki eksperymentów i ocenę jakości optymalnej trasy dostaw.
