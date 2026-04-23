# Ekonometria danych panelowych

Repozytorium zawiera projekt zespołowy z zakresu ekonometrii danych panelowych dotyczący analizy zależności między stopą bezrobocia a wybranymi czynnikami społeczno-ekonomicznymi w krajach Unii Europejskiej.

## Autorzy

Projekt zrealizowany wspólnie przez:

- Kinga Kołodziej
- Julię Matyję

## Zakres projektu

W projekcie przeprowadzono:
- przygotowanie panelowego zbioru danych dla 26 krajów Unii Europejskiej z lat 2015–2023,
- wstępną analizę danych,
- estymację modelu regresji łącznej (pooled OLS),
- estymację modeli panelowych z efektami ustalonymi (FE) i losowymi (RE), w wersji jednokierunkowej i dwukierunkowej,
- porównanie modeli z wykorzystaniem testu F, testu Breuscha–Pagana oraz testu Hausmana,
- weryfikację modelu, obejmującą badanie autokorelacji, zależności przekrojowej, heteroskedastyczności i normalności reszt,
- zastosowanie odpornych błędów standardowych,
- estymację modelu dynamicznego z opóźnioną zmienną zależną,
- estymację dynamicznego modelu panelowego metodą Arellano-Bonda (GMM).

## Zawartość repozytorium

- `EDP.Rmd` – plik źródłowy analizy w R Markdown
- `EDP.pdf` – raport końcowy
- `EDP.csv` – dane wejściowe wykorzystane w projekcie
