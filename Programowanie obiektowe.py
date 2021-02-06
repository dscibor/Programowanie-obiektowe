# class Dlugopis:
#     def __init__(self, waga, wysokosc, srednica ,kolor ,kolor_w, cena):
#         self.waga = 15
#         self.wysokosc = 12
#         self.srednica = 1
#         self.kolor = pomaranczowy
#         self.kolor_w = niebieski
#         self.cena = 1.20

class Zwierze:
    def __init__(self, gatunek = "", imie = "", wiek = 0):
        self.gatunek = gatunek
        self.imie = imie
        self.wiek = wiek

    def dodaj_gatunek(self, gatunek):
        gatunek = input("Podaj gatunek: ")
        

    def dodaj_imie(self, imie):
        imie = input("Podaj imie: ")

    def dodaj_wiek(self, wiek):
        wiek = input("Podaj wiek: ")

    def zwierzak(self):
        print(self.gatunek, self.imie, self.wiek)

print("Dodaj zwierzę")
gatunek = input("Podaj gatunek zwierzęcia: ")
imie = input("Podaj imię zwierzęcia: ")
wiek = input("Podaj wiek zwierzęcia: ")
zwierzak = Zwierze(gatunek, imie ,wiek)
print(zwierzak.gatunek, zwierzak.imie, zwierzak.wiek)



