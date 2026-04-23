# Ekonometryczny model stopy bezrobocia

Repozytorium zawiera projekt ekonometryczny dotyczący analizy stopy bezrobocia w powiatach w Polsce z wykorzystaniem modeli regresji liniowej w programie Gretl.

## Zakres analizy

W projekcie przeprowadzono:
- statystyki opisowe,
- analizę wykresów zależności,
- macierz korelacji,
- estymację modelu OLS,
- analizę współliniowości (VIF),
- metodę Hellwiga,
- metodę krokową wsteczną,
- transformację logarytmiczną zmiennych,
- ocenę efektu katalizy,
- test normalności reszt,
- test White’a,
- testy pominiętych zmiennych,
- test serii,
- test RESET,
- test Chowa,
- analizę koincydencji,
- prognozę punktową wraz z 95% przedziałem ufności.

## Zawartość repozytorium

- `EKONOMETRYCZNY MODEL STOPY BEZROBOCIA.pdf` – pełny raport z projektu
- `skrypt.inp` – skrypt Gretla wykorzystany do analizy
- `dane.gdt` – główny zbiór danych
- `dane_test_chowa.gdt` – zbiór danych wykorzystany do testu Chowa
