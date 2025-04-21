# Assignment 1: Design Your Own Class (Superhero Example)

class Superhero:
    def __init__(self, name, power, origin):
        self._name = name  
        self._power = power
        self._origin = origin

    def show_identity(self):
        print(f"I am {self._name} from {self._origin} ")
    
    def use_power(self):
        print(f"{self._name} uses {self._power}! ")

# Inherited class with polymorphism
class SpeedHero(Superhero):
    def use_power(self):
        print(f"{self._name} zooms past at lightning speed! ")

# Another inherited class
class WaterHero(Superhero):
    def use_power(self):
        print(f"{self._name} controls waves with incredible force! ")

# Creating objects
hero1 = SpeedHero("FlashNova", "Super Speed", "Velocity Valley")
hero2 = WaterHero("AquaFury", "Hydrokinesis", "Ocean Depths")

hero1.show_identity()
hero1.use_power()

hero2.show_identity()
hero2.use_power()

