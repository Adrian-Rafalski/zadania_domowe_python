
class Uczen:
    def __init__(self, imie, nazwisko, klasa_ucznia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa_ucznia

    def __repr__(self):
        return f"Uczeń {self.imie} {self.nazwisko} z klasy {self.klasa}"


class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot_nauczania, klasa_nauczyciela):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot_nauczania = przedmiot_nauczania
        self.klasa_nauczyciela = klasa_nauczyciela

    def __repr__(self):
        return f"Nauczyciel {self.imie} {self.nazwisko} naucza przedmiotu {self.przedmiot_nauczania} w klasach {self.klasa_nauczyciela} "


class Wychowawca:
    def __init__(self, imie, nazwisko, klasa_wychowawcy):
        self.imie = imie
        self.nzawisko = nazwisko
        self.klasa = klasa_wychowawcy

    def __repr__(self):
        return f"Wychowawca {self.imie} {self.nzawisko} opiekuje się klasą {self.klasa}"

class Klasa:
    def __init__(self, numer_klasy, imie_ucznia, nazwisko_ucznia, imie_wychowawcy, nazwisko_wychowawcy):
        self.numer_klasy = numer_klasy
        self.imie_ucznia = imie_ucznia
        self.nazwisko_ucznia = nazwisko_ucznia
        self.imie_wychowawcy = imie_wychowawcy
        self.nazwisko_wychowawcy = nazwisko_wychowawcy

    def __repr__(self):
        return f"W klasie o numerze {self.numer_klasy} uczniami są {self.imie_ucznia} {self.nazwisko_ucznia} natomiast wychowawcą jest {self.imie_wychowawcy} {self.nazwisko_wychowawcy}"

def wyszukanie_klasy_i_przedmiotow_ucznia(imie, nazwisko, przedmioty):
    for uczen in przedmioty:
        if uczen.imie == imie and uczen.nazwisko == nazwisko:
            return uczen.przedmiot_nauczania

def podanie_listy_uczniow_po_numerze_klasy(numer_klasy, lista_uczniow):
    uczniowie_w_klasie = []
    for uczen in lista_uczniow:
        if uczen.klasa == numer_klasy:
            uczniowie_w_klasie.append(uczen)
        return uczniowie_w_klasie

szkola = {
    "uczniowie": [Uczen("Adam", "Małysz", "3C"), Uczen("Domino", "Jachaś", "3C"), Uczen("Julian", "Król", "6A")],
    "Nauczyciele": [Nauczyciel("Anna", "Wojna", "Biologia", ["3C", "6A"]), Nauczyciel("Jerzy", "Ważny", "Chemia", ["6A"]), Nauczyciel("Daria", "Liczydło", "Matematyka", ["3C"])],
    "Wychowawcy": [Wychowawca("Grażyna", "Pierzyna", "3C"), Wychowawca("Wojciech", "Noga", "6A")],
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
            szkola["uczniowie"].append(Uczen(imie, nazwisko, klasa))
            szkola["klasy"].append(Klasa(klasa, imie, nazwisko, "", ""))

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
            szkola["Wychowawcy"].append(Wychowawca(imie, nazwisko , klasa_wychowawcy))

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
            if imie_ucznia in szkola["uczniowie"] and nazwisko_ucznia in szkola["uczniowie"]:
                print("Bedzie dzialac")

        elif zarzadzanie == "2" or zarzadzanie == "Klasa":
            numer_klasy = input("Podaj numer klasy aby wyświetlić jej uczniów: ")
            if numer_klasy in szkola["klasy"]:
                print(f"Uczniowie klasy {numer_klasy}: {szkola['klasy'][numer_klasy]}")




    elif menu_glowne == "3" or menu_glowne == "Koniec":
        print("Koniec")
        koniec_programu = True
