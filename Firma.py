
class Human:
    def __init__(self, imie:str, nazwisko:str, wiek:int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    
    def ___str__(self):
        return str(self.__dict__)

    def przywitaj_sie(self):
        print("Witam!")

    def wiek_ale_w_miesiacach(self):
        wiek_w_m = (self.wiek * 12)
        return wiek_w_m

class Employee(Human):
    def __init__(self, imie:str, nazwisko:str, wiek:int, pensja:float, numer_identyfikacyjny:int, szef = None):
        Human.__init__(self, imie, nazwisko, wiek)
        self.pensja = pensja
        self.numer_identyfikacyjny = numer_identyfikacyjny
        self.szef = szef

    def oblicz_pensje_roczna(self):
        pensja_roczna = (self.pensja * 12)
        return pensja_roczna

    def ___str__(self):
        return str(self.__dict__)

pracownik1 = Employee("Danuta", "Zdupy", 30, 1900.8, 21)
pracownik2 = Employee("Zbigniew", "Zdupa", 35, 1910.9, 20, pracownik1)
print(str(pracownik1.___str__()))
print(pracownik1.oblicz_pensje_roczna())