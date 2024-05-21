# Program generujący życzenia urodzinowe
import datetime
import sys



while True:
    imie_odbiorcy = input("Podaj imię solenizanta: ")
    if imie_odbiorcy.isalpha():
        break
    if imie_odbiorcy.isdigit():
        print("Imiona nie mają cyfr. Wprowadź poprawne dane")
        continue


while True:
    rok_urodzenia = input("Podaj rok urodzenia solenizanta: ")
    rok = rok_urodzenia
    if rok.isalpha():
        print("Rok urodzenia musi zawierać jedynie cyfry. Popraw swoje dane")
        continue
    rok =int(rok)
    if rok < 0:
        print("Rok urodzenia nie może być ujemny. Wprowadź poprawne dane")
        continue
    if rok_urodzenia.isdigit():
        break


def input_multiline(prompt=''):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)
zyczenia = input_multiline("Wpisz swoje życzenia urodzinowe. Aby zakończyć, wciśnij Enter na pustej linii: ")

while True:
    imie_nadawcy = input("Wpisz swoje imię: ")
    if imie_nadawcy.isdigit():
        print("Imiona nie mają cyfr. Wprowadź poprawne dane")
        continue
    if imie_nadawcy.isalpha():
        break


aktualna_data = datetime.datetime.now()
obecny_rok = aktualna_data.year
wiek = (obecny_rok - rok)

print(f'''{imie_odbiorcy}, wszystkiego najlepszego z okazji {wiek} urodzin!

{zyczenia}

{imie_nadawcy}''')
