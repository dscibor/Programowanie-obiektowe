
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

class Business:
    def __init__(self, nazwa:str, branza:str, lista_pracownikow:list):
        self.nazwa = nazwa
        self.branza = branza
        self.lista_pracownikow = lista_pracownikow

        
    def dodaj_pracownika(self, pracownik:Employee):
        self.lista_pracownikow.append(pracownik)

    def usun_pracownika_o_numerze(self, pracownik):
        pass
    def usun_pracownika(self, lista_pracownikow):
        pass
    def policz_pracownikow(self, lista_pracownikow):
        pass

    





