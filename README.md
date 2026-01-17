# Symulator Poszukiwacza Skarbów (SKARBFI)

## Opis
Projekt jest symulacją logiczną problemu [SPOJ SKARBFI](https://pl.spoj.com/problems/SKARBFI/).
Program generuje losową ścieżkę poszukiwacza (złożoną z kierunków Północ, Południe, Wschód, Zachód), a następnie oblicza **wypadkowe przemieszczenie**.

Celem algorytmu jest stwierdzenie, gdzie znajduje się skarb względem punktu startu i podanie najkrótszej drogi do niego (lub informacji, że jest to punkt startowy - "Studnia").

## Jak to działa?
Algorytm sumuje kroki w przeciwległych kierunkach i redukuje je:
1.  Zlicza sumę kroków dla osi Y (Północ vs Południe).
2.  Zlicza sumę kroków dla osi X (Wschód vs Zachód).
3.  Oblicza różnicę (netto).

Jeśli poszukiwacz poszedł 5 kroków na Północ i 3 na Południe, wynik to **2 kroki na Północ**.

## Uruchomienie
Wymagany Python 3.

```bash
python main.py
