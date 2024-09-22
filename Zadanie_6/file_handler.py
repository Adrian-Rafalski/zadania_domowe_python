import json


class FileHandler:
    def __init__(self, plik_danych, plik_przegladu):
        self.plik_danych = plik_danych
        self.plik_przegladu = plik_przegladu

    def zaladuj_dane_z_plliku_danych(self):
        with open(self.plik_danych) as file:
            return json.loads(file.read())

    def zaladuj_historie_z_pliku_przegladu(self):
        with open(self.plik_przegladu) as file:
            return json.loads(file.read())

    def zapisz_dane_do_pliku_danych(self, dane):
        with open(self.plik_danych, mode="w") as file:
            file.write(json.dumps(dane))

    def zapisz_historie_do_pliku_przegladu(self, przeglad):
        with open(self.plik_przegladu, mode="w") as file:
            file.write(json.dumps(przeglad))
