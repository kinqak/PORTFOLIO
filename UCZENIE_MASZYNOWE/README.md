# Predykcja decyzji rekrutacyjnych z wykorzystaniem metod uczenia maszynowego

Repozytorium zawiera projekt zespołowy z zakresu uczenia maszynowego dotyczący predykcji decyzji rekrutacyjnych na podstawie cech kandydatów, wyników ocen oraz strategii rekrutacyjnej.

## Autorzy

Projekt zrealizowany wspólnie przez:
- Kinga Kołodziej
- Julię Matyję

## Zakres projektu

W projekcie przeprowadzono:
- eksploracyjną analizę danych,
- analizę braków danych, zbalansowania zbioru i wartości odstających,
- przygotowanie danych do modelowania, w tym podział na zbiór treningowy i testowy oraz kodowanie zmiennych kategorycznych,
- walidację krzyżową i strojenie hiperparametrów,
- budowę i porównanie modeli: regresji logistycznej, kNN, kkNN, drzewa decyzyjnego, lasu losowego, XGBoost oraz SVM,
- wybór najlepszego modelu na podstawie metryk jakości klasyfikacji,
- analizę interpretowalności modelu z wykorzystaniem:
  - ważności zmiennych,
  - profili ceteris paribus,
  - wykresów częściowej zależności (PDP),
  - wykresów break-down,
  - wartości SHAP.

## Zawartość repozytorium

- `UM.Rmd` – plik źródłowy analizy w R Markdown
- `UM.pdf` – raport końcowy
- `recruitment_data.csv` – dane wejściowe wykorzystane w projekcie
