
class Uczen:
    def __init__(self, imie, nazwisko, klasa_ucznia, przedmiot):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa_ucznia = klasa_ucznia
        self.przedmiot_ucznia = przedmiot

    def __repr__(self):
        return (f"Uczeń {self.imie} {self.nazwisko} z klasy {self.klasa_ucznia}"
                f" uczęszcza na następujące lekcje: {self.przedmiot_ucznia}")


class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot_nauczania, klasa_nauczyciela):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot_nauczania = przedmiot_nauczania
        self.klasa_nauczyciela = klasa_nauczyciela

    def __repr__(self):
        return (f"Nauczyciel {self.imie} {self.nazwisko} naucza przedmiotu {self.przedmiot_nauczania}"
                f" w klasach {self.klasa_nauczyciela} ")


class Wychowawca:
    def __init__(self, imie, nazwisko, klasa_wychowawcy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa_wychowawcy = klasa_wychowawcy

    def __repr__(self):
        return f"Wychowawca {self.imie} {self.nazwisko} opiekuje się klasą {self.klasa_wychowawcy}"


class Klasa:
    def __init__(self, numer_klasy, imie_ucznia, nazwisko_ucznia, imie_wychowawcy, nazwisko_wychowawcy):
        self.numer_klasy = numer_klasy
        self.imie_ucznia = imie_ucznia
        self.nazwisko_ucznia = nazwisko_ucznia
        self.imie_wychowawcy = imie_wychowawcy
        self.nazwisko_wychowawcy = nazwisko_wychowawcy

    def __repr__(self):
        return (f"W klasie o numerze {self.numer_klasy} uczniami są {self.imie_ucznia} {self.nazwisko_ucznia} "
                f"natomiast wychowawcą jest {self.imie_wychowawcy} {self.nazwisko_wychowawcy}")

# def wyszukanie_klasy_po_imienieu_i_nazwisku_ucznia(imie, nazwisko, klasa):
#     for uczen in klasa:
#         if uczen.imie == imie and uczen.nazwisko == nazwisko:
#             return uczen.klasa_ucznia


def podanie_listy_uczniow_po_numerze_klasy(numer_klasy, lista_uczniow):
    lista_uczniow_w_klasie = []
    for uczen in lista_uczniow:
        if uczen.klasa_ucznia == numer_klasy:
            lista_uczniow_w_klasie.append(uczen)
    return lista_uczniow_w_klasie


def podanie_wychowawcy_po_numerze_klasy(numer_klasy, lista_wychowawcow):
    for wychowawca in lista_wychowawcow:
        if wychowawca.klasa_wychowawcy == numer_klasy:
            return wychowawca


def wyszukanie_przedmiotow_po_imieniu_i_nazwisku_ucznia(imie, nazwisko, lista_uczniow):
    for uczen in lista_uczniow:
        if uczen.imie == imie and uczen.nazwisko == nazwisko:
            return uczen.przedmiot_ucznia


# def wyszukanie_nauczyciela_po_nazwie_przedmiotu(nazwa_przedmiotu, lista_nauczycieli):
#     for nauczyciel in lista_nauczycieli:
#         if nazwa_przedmiotu in nazwa_przedmiotu.przedmiot_nauczania:
#             return nauczyciel


def wyszukanie_klas_po_imieniu_i_nazwisku_nauczyciela(imie, nazwisko, lista_klas):
    lista_klas_nauczyciela = []
    for nauczyciel in lista_klas:
        if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
            lista_klas_nauczyciela.append(nauczyciel)
    return lista_klas_nauczyciela


def wyszukiwanie_klasy_po_wychowawcy(imie, nazwisko, lista_wychowawcow):
    for wychowawca in lista_wychowawcow:
        if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko:
            return wychowawca.klasa_wychowawcy


szkola = {
    "Uczniowie": [Uczen("Adam", "Kos", "3C", ["Biologia", "Chemia"]), Uczen("Kamil", "Zdun", "3C", ["Chemia"]), Uczen("Domino", "Jachaś", "6A", ["Matematyka", "Chemia"])],
    "Nauczyciele": [Nauczyciel("Anna", "Wojna", "Biologia", ["3C", "6A"]), Nauczyciel("Jerzy", "Ważny", "Chemia", ["6A"]), Nauczyciel("Daria", "Liczydło", "Matematyka", ["3C"])],
    "Wychowawcy": [Wychowawca("Anna", "Wad", "3C"), Wychowawca("Wojciech", "Noga", "6A")],
    "klasy": [Klasa("3C", "Adam", "Małysz", "Grażyna", "Pierzyna"), Klasa("6A", "Julian", "Król", "Wojciech", "Noga")]
}

koniec_programu = False
print("Witaj w szkole podstawowej im. 'Tego którego imienia nie wolno wymawiać'")

while not koniec_programu:
    menu_glowne = input("Wpisz polecenie które chcesz wykonać: \n"
                        "1. Utwórz\n"
                        "2. Zarządzaj\n"
                        "3. Koniec\n")

    if menu_glowne == "1" or menu_glowne == "Utwórz":
        tworzenie = input("Jakiego użytkownika chcesz dodać do systemu? \n"
                          "1. Uczeń\n"
                          "2. Nauczyciel\n"
                          "3. Wychowawca\n"
                          "4. Koniec\n")
        if tworzenie == "1" or tworzenie == "Uczeń":
            imie = input("Podaj imię nowego ucznia: ")
            nazwisko = input("Podaj nazwisko nowego ucznia: ")
            klasa = input("Podaj klasę do której uczęszcza uczeń: ")
            lista_przedmiotow = []
            nowy_przedmiot = True
            while nowy_przedmiot:
                lekcje = input("Podaj przedmioty na jakie uczęszcza uczeń potwierdzając każdy z nich klawiszem Enter: ")
                if lekcje:
                    lista_przedmiotow.append(lekcje)
                else:
                    nowy_przedmiot = False
            szkola["Uczniowie"].append(Uczen(imie, nazwisko, klasa, lista_przedmiotow))

        elif tworzenie == "2" or tworzenie == "Nauczyciel":
            imie = input("Podaj imię nauczyciela: ")
            nazwisko = input("Podaj nazwisko nauczyciela: ")
            przedmiot = input("Podaj przedmiot którego uczy nauczyciel: ")
            lista_klas = []
            nowa_klasa = True
            while nowa_klasa:
                klasa = input("Podaj klasy w których uczy nauczyciel potwierdzając każdą klawiszem Enter: ")
                if klasa:
                    lista_klas.append(klasa)
                else:
                    nowa_klasa = False
            szkola["Nauczyciele"].append(Nauczyciel(imie, nazwisko, przedmiot, lista_klas))

        elif tworzenie == "3" or tworzenie == "Wychowawca":
            imie = input("Podaj imię wychowawcy: ")
            nazwisko = input("Podaj nazwisko wychowawcy: ")
            klasa_wychowawcy = input("Podaj numer klasy którą opiekuje się wychowawca: ")
            szkola["Wychowawcy"].append(Wychowawca(imie, nazwisko, klasa_wychowawcy))
            szkola["klasy"].append(Klasa("", "", "", imie, nazwisko))

        elif tworzenie == "4" or tworzenie == "Koniec":
            continue

    if menu_glowne == "2" or menu_glowne == "Zarządzaj":
        zarzadzanie = input("Jakim użytkownikiemchcesz zarządzać? \n"
                            "1. Uczeń\n"
                            "2. Klasa\n"
                            "3. Nauczyciel\n"
                            "4. Wychowawca\n"
                            "5. Koniec\n")
        if zarzadzanie == "1" or zarzadzanie == "Uczeń":
            imie_ucznia = input("Podaj imię ucznia: ")
            nazwisko_ucznia = input("Podaj nazwisko ucznia: ")
            zajecia_ucznia = (wyszukanie_przedmiotow_po_imieniu_i_nazwisku_ucznia(imie_ucznia, nazwisko_ucznia, szkola.get("Uczniowie")))
            print(f"Uczeń {imie_ucznia} {nazwisko_ucznia} uczęszcza na zajęcia: {zajecia_ucznia}")
            # nauczyciel_przedmiotu = (wyszukanie_nauczyciela_po_nazwie_przedmiotu(zajecia_ucznia, szkola.get("Nauczyciele")))
            # print(nauczyciel_przedmiotu)

        elif zarzadzanie == "2" or zarzadzanie == "Klasa":
            numer_klasy_do_sprawdzenia = input("Podaj numer klasy aby wyświetlić jej uczniów: ")
            print(podanie_listy_uczniow_po_numerze_klasy(numer_klasy_do_sprawdzenia, szkola.get("Uczniowie")))
            print(podanie_wychowawcy_po_numerze_klasy(numer_klasy_do_sprawdzenia, szkola.get("Wychowawcy")))

        elif zarzadzanie == "3" or zarzadzanie == "Nauczyciel":
            imie = input("Podaj imię nauczyciela: ")
            nazwisko = input("Podaj nazwisko nauczyciela: ")
            print(wyszukanie_klas_po_imieniu_i_nazwisku_nauczyciela(imie, nazwisko, szkola.get("Nauczyciele")))

        elif zarzadzanie == "4" or zarzadzanie == "Wychowawca":
            imie = input("Podaj imię wychowawcy: ")
            nazwisko = input("Podaj nazwisko wychowawcy: ")
            klasa_wychowawcy = (wyszukiwanie_klasy_po_wychowawcy(imie, nazwisko, szkola.get("Wychowawcy")))
            print(f"Nauczyciel {imie} {nazwisko} jest wychowawcą klasy {klasa_wychowawcy}")
            lista_uczniow_wychowawcy = (podanie_listy_uczniow_po_numerze_klasy(klasa_wychowawcy, szkola.get("Uczniowie")))
            print(f"W klasie wychowawcy znajdują się: {lista_uczniow_wychowawcy}")

        elif zarzadzanie == "5" or zarzadzanie == "Koniec":
            continue

    elif menu_glowne == "3" or menu_glowne == "Koniec":
        print("Koniec")
        koniec_programu = True
