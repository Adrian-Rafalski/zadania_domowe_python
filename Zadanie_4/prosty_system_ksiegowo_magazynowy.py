
przeglad = []
saldo = 10000
stan_magazynu = [
    {
        "nazwa_artykulu": "Watroba Marsjanina",
        "numer_ewidencyjny": "123456",
        "cena": 3000,
        "ilosc_na_magazynie": 5
    },
    {
        "nazwa_artykulu": "Statek kosmiczny",
        "numer_ewidencyjny": "67867",
        "cena": 15000,
        "ilosc_na_magazynie": 1
    },
    {
        "nazwa_artykulu": "Laserowy Minigun",
        "numer_ewidencyjny": "457645",
        "cena": 9999,
        "ilosc_na_magazynie": 7
    }
]
program_trwa = True

print("Witaj w magazynie 'Strefa 51'")

while program_trwa:
    polecenie = int(input("Wybierz co chcesz zrobić.\n"
                                  "1. Saldo\n"
                                  "2. Sprzedaż\n"
                                  "3. Zakup\n"
                                  "4. Konto\n"
                                  "5. Lista\n"
                                  "6. Magazyn\n"
                                  "7. Przegląd\n"
                                  "8. Koniec\n"))
    if polecenie == 1:
        zmiana_salda = float(input("Podaj proszę kwotę o jaką chcesz zmienić nasze saldo: "))
        if -zmiana_salda > saldo:
            print("Niestety nie możesz wypłacić takich środków! Saldo nie może być ujemne!")
            continue
        saldo += zmiana_salda
        przeglad.append("Dodanie kwoty do salda")

    elif polecenie == 2:
        nazwa_produktu = input("Podaj proszę nazwę artykułu który chcesz kupić: ")
        ilosc_do_zakupu = int(input("Podaj proszę ile sztuk chcesz kupić: "))
        znaleziony_produkt = False
        for produkt in stan_magazynu:
            if produkt.get("nazwa_artykulu") == nazwa_produktu:
                znaleziony_produkt = True
                if produkt.get("ilosc_na_magazynie") - ilosc_do_zakupu >= 1:
                    produkt["ilosc_na_magazynie"] -= ilosc_do_zakupu
                    saldo += produkt.get("cena")
                    print(f"Udało Ci się kupić: {ilosc_do_zakupu} szt. artykułu: {produkt.get('nazwa_artykulu')}")
                else:
                    print("Niestety nie mamy tylu sztuk na stanie. Spróbuj kupić mniejszą ilość lub zaczekaj na dostawę")
        if not znaleziony_produkt:
            print("Niestety nie mamy na magazynie takiego artykułu")

    elif polecenie == 4:
        print(f"Saldo magazynu wynosi: {saldo}")

    elif polecenie == 5:
        print(f"Dane twojej księgarni:")
        for produkt in stan_magazynu:
            print(produkt)

    elif polecenie == 6:
        nazwa_produktu = input("Podaj proszę nazwę artykułu którego stan magazynowy chcesz wyświetlić: ")
        znaleziony_produkt = False
        for produkt in stan_magazynu:
            if produkt.get("nazwa_artykulu") == nazwa_produktu:
                print(f"Stan magazynu wynosi: {produkt.get("ilosc_na_magazynie")} szt.")
                znaleziony_produkt = True
                break
        if not znaleziony_produkt:
            print("Niestety nie mamy artykulu o takiej nazwie")

    elif  polecenie == 8:
        program_trwa = False
        print("Koniec pracy")

