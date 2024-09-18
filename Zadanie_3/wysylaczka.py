# Program do obsługi ładowarki paczek

print("Witaj w firmie kurierskiej 'Tam i z powrotem'")
liczba_przedmiotow = int(input("Podaj liczbę przedmiotów do wysłania: "))

waga_sumaryczna = 0
obecna_waga_paczki = 0
maksymalna_waga_paczki = 20
ilosc_paczek = []

for n in range(liczba_przedmiotow):
    waga_przedmiotu = int(input("Podaj wagę każdego z przedmiotów: "))
    if 1 <= waga_przedmiotu <= 10:
        waga_sumaryczna += int(waga_przedmiotu)
    else:
        print("Waga paczki nieprawidłowa, robię wysyłkę")
        break
