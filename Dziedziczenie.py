
class Animal:
    def __init__(self): 
        pass

    def sleep(self):
        print("Zzz")

    def makeNoise(self):
        print("Arrrr!")
        
class Chicken(Animal):

    def make_eggs(self):
        print("Egg")

    def makeNoise(self):
        print("KUKURYKU")

class Dog(Animal):

    def makeNoise(self):
        print("Wrrrr! HAU")

    def defensive(self):
        print("Armor 5")

class Cat(Animal):

    def makeNoise(self):
        print("Miau")

    def defensive(self):
        print("Armor 1")
    
class Bambi(Dog):

    def makeNoise(self):
        print("wrrrr hau")

z_chicken = Chicken()
z_object = Animal()
z_dog = Dog()
z_cat = Cat()
z_bambi = Bambi()

z_dog.makeNoise()
z_dog.defensive()
z_cat.makeNoise()
z_cat.defensive()
z_bambi.makeNoise()



    