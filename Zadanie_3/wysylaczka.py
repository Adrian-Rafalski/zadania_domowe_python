# Program do obsługi ładowarki paczek

print("Witaj w firmie kurierskiej 'Tam i z powrotem'")
liczba_przedmiotow = int(input("Podaj liczbę przedmiotów do wysłania: "))

waga_sumaryczna = 0
ilosc_paczek = 1
maksymalna_waga_paczki = 20
obecna_waga_paczki = 0
ilosc_wolnego_miejsca = 0
numer_paczki_z_max_pustym_miejscem = 1
ilosc_nadanych_paczek = 0

for n in range(liczba_przedmiotow):
    waga_przedmiotu = int(input("Podaj wagę każdego z przedmiotów: "))
    if 1 <= waga_przedmiotu <= 10:
        ilosc_nadanych_paczek += 1
        waga_sumaryczna += waga_przedmiotu
        if waga_przedmiotu + obecna_waga_paczki > maksymalna_waga_paczki:
            if maksymalna_waga_paczki - obecna_waga_paczki > ilosc_wolnego_miejsca:
                ilosc_wolnego_miejsca = maksymalna_waga_paczki - obecna_waga_paczki
                numer_paczki_z_max_pustym_miejscem = ilosc_paczek
            ilosc_paczek += 1
            obecna_waga_paczki = waga_przedmiotu
        else:
            obecna_waga_paczki += waga_przedmiotu
    else:
        print("Waga przedmiotu nie mieści się w przedziale wagowym 1-10 kg, robię wysyłkę \n")
        break
if maksymalna_waga_paczki - obecna_waga_paczki > ilosc_wolnego_miejsca:
    ilosc_wolnego_miejsca = maksymalna_waga_paczki - obecna_waga_paczki
    numer_paczki_z_max_pustym_miejscem = ilosc_paczek

print(f"Suma wysłanych kilogramów {waga_sumaryczna}")
print(f"Ilość wysłanych paczek: {ilosc_paczek}")
print(f"Suma 'pustych' kilogramów {ilosc_paczek * maksymalna_waga_paczki - waga_sumaryczna}")
print(f"Największa ilość niewykorzystanych kilogramów: {ilosc_wolnego_miejsca}, w paczce o numerze: {numer_paczki_z_max_pustym_miejscem}")
