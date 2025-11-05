import weapon
from abc import ABC, abstractmethod

class StrikeOption(ABC):
    def __init__(self, name: str, ammo: int):
        self.name: str = name
        self.ammo: int = ammo

    @abstractmethod
    def strike(self):
        pass

class Tank(StrikeOption):
    def __init__(self, name: str, ammo: int):
        super().__init__(name, ammo)


    def strike(self):
        print('Im the Tank class and..... strike')

class Drone(StrikeOption):
    def __init__(self, name: str, ammo: int):
        super().__init__(name, ammo)

    def strike(self):
        print('Im the Drone class and..... strike')


weapon1 = weapon.Weapon('M16', 90)
weapon2 = weapon.Weapon('usi', 900)
soldier1 = weapon.Soldier('Meir', 'samal', weapon1)
soldier2 = weapon.Soldier('David', 'turai', weapon2)
soldier3 = weapon.Soldier('Samuel', 'turai', weapon1)
commander = weapon.Soldier('Libero', 'seren', weapon1)
soldiers = [soldier1, soldier2, soldier3]
tank = Tank('mercava3', 300)
drone = Drone('F-16', 34)
unit1 = weapon.Unit("8200", commander, soldiers, [tank, drone])

for strike in unit1.strike:
    strike.strike()












