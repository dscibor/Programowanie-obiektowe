
filename = "MojaFarma.txt"

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

def get_zwierzaki_from_file(filename):
    zwierzaki = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                l = line.rstrip('\n')
                lista_slow = l.split(' ') 
                gatunek = lista_slow[0]
                imie = lista_slow[1]
                wiek = lista_slow[2]
                zwierzak = Zwierze(gatunek, imie, wiek)
                zwierzaki.append(zwierzak)
    except:
        print("Nie ma takiego pliku!")
    return zwierzaki

def clear_lista(filename):
    with open(filename, 'w') as file:
        pass

def save_zwierzaki_to_file(filename, zwierzaki):
    with open(filename, 'w') as file:
        for zwierzak in zwierzaki:
            file.write('{} {} {}\n'.format(zwierzak.gatunek, zwierzak.imie, zwierzak.wiek))

zwierzaki = get_zwierzaki_from_file(filename)

for element in zwierzaki:
    print(element.gatunek, element.imie, element.wiek)

print("\n")
print("Dodaj zwierzę")
gatunek = input("Podaj gatunek zwierzęcia: ")
imie = input("Podaj imię zwierzęcia: ")
wiek = input("Podaj wiek zwierzęcia: ")

if gatunek == "clear" or imie == "clear" or wiek == "clear":
    clear_lista(filename)
    print("Wyczyszczono farmę!")
else:
    zwierzak = Zwierze(gatunek, imie ,wiek)
    zwierzaki.append(zwierzak)
    print(zwierzak.gatunek, zwierzak.imie, zwierzak.wiek)

    save_zwierzaki_to_file(filename, zwierzaki)
    



