przeglad = []
saldo = 100000
stan_magazynu = [
    {
        "nazwa_artykulu": "Watroba Marsjanina",
        "cena": 3000,
        "ilosc_na_magazynie": 5
    },
    {
        "nazwa_artykulu": "Statek kosmiczny",
        "cena": 15000,
        "ilosc_na_magazynie": 1
    },
    {
        "nazwa_artykulu": "Laserowy Minigun",
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
        przeglad.append("Zmiana obecnego salda")

    elif polecenie == 2:
        nazwa_produktu = input("Podaj proszę nazwę artykułu który chcesz sprzedać: ")
        ilosc_do_sprzedazy = int(input("Podaj proszę ile sztuk chcesz sprzedać: "))
        znaleziony_produkt = False
        for produkt in stan_magazynu:
            if produkt.get("nazwa_artykulu") == nazwa_produktu:
                znaleziony_produkt = True
                if produkt.get("ilosc_na_magazynie") - ilosc_do_sprzedazy >= 1:
                    produkt["ilosc_na_magazynie"] -= ilosc_do_sprzedazy
                    saldo += produkt.get("cena")
                    print(f"Udało Ci się sprzedać: {ilosc_do_sprzedazy} szt. artykułu: {produkt.get('nazwa_artykulu')}")
                else:
                    print(
                        "Niestety nie mamy tylu sztuk na stanie. "
                        "Spróbuj kupić mniejszą ilość lub zaczekaj na dostawę")
                przeglad.append("Sprzedano artykul")
        if not znaleziony_produkt:
            print("Niestety nie mamy na magazynie takiego artykułu")

    elif polecenie == 3:
        artykul = input("Podaj nazwę artykułu: ")
        cena_zakupu = float(input("Podaj koszt zakupu jednej sztuki produktu: "))
        ilosc_do_zakupu = int(input("Podaj ilość sztuk do zakupienia: "))
        stan_magazynu.append(
            {
                "nazwa_artykulu": artykul,
                "cena": cena_zakupu,
                "ilosc_na_magazynie": ilosc_do_zakupu
            })

        saldo -= ilosc_do_zakupu * cena_zakupu
        przeglad.append("Zakup nowego artykulu")
        print(f"Gratulacje na stan magazynu dodane zostało {ilosc_do_zakupu} szt. artykułu {artykul}")

    elif polecenie == 4:
        print(f"Saldo magazynu wynosi: {saldo}")
        przeglad.append("Wyswietlono saldo magazynu")

    elif polecenie == 5:
        print(f"Informacje o stanie magazynowym:")
        for produkt in stan_magazynu:
            print(produkt)
        przeglad.append("Wyświetlono stan magazynowy")

    elif polecenie == 6:
        nazwa_produktu = input("Podaj proszę nazwę artykułu którego stan magazynowy chcesz wyświetlić: ")
        znaleziony_produkt = False
        for produkt in stan_magazynu:
            if produkt.get("nazwa_artykulu") == nazwa_produktu:
                print(f"Stan magazynu wynosi: {produkt.get("ilosc_na_magazynie")} szt.")
                znaleziony_produkt = True
                break
            przeglad.append("Wyświetlono szczeguły artykulu na magazynie")
        if not znaleziony_produkt:
            print("Niestety nie mamy artykulu o takiej nazwie")

    elif polecenie == 7:
        od = input("Podaj poczatkowy zakres historii: ")
        do = input("Podaj koncowy zakres historii: ")

        if od == "":
            poczatek = 0
        else:
            poczatek = int(od)

        if do == "":
            koniec = len(przeglad)
        else:
            koniec = int(do) + 1

        if poczatek < 0 or koniec > len(przeglad) or poczatek >= koniec:
            print(f"Podano niewłaściwy zakres historii. Liczba wpisów wynosi: {len(przeglad)}")
            continue

        print("Oto spis akcji przeprowadzonych w magazynie w wybranym zakresie")
        for zakres in range(poczatek, koniec):
            print(f"{zakres}: {przeglad[zakres]}")
        przeglad.append("Dokonano przeglądu historii")
    elif polecenie == 8:
        program_trwa = False
        print("Koniec pracy")
