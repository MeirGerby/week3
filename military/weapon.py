from abc import abstractmethod
from random import randint
from strike_option import StrikeOption
class Weapon:
    total_weapons: int = 0
    def __init__(self, name: str, ammo: int):
        self.name: str = name
        self.ammo: int = ammo
        self.max_ammo = 500
        Weapon.total_weapons += 1

    def reload(self, amount):
        self.ammo += amount
        if self.ammo > self.max_ammo:
            self.ammo = self.max_ammo

weapon1 = Weapon('M16', 90)
# weapon2 = weapon.Weapon('usi', 900)
# soldier1 = weapon.Soldier('Meir', 'samal', weapon1)
# soldier2 = weapon.Soldier('David', 'turai', weapon2)
# soldier3 = weapon.Soldier('Samuel', 'turai', weapon1)
# commander = weapon.Soldier('Libero', 'seren', weapon1)


class Soldier:
    def __init__(self, name: str, rank: str, weapon: Weapon):
        self.name: str = name
        self.rank: str = rank
        self.weapon: Weapon = weapon

    def report(self):
        print(f'--Soldier--'
              f'Name: {self.name}'
              f'Rank: {self.rank}'
              f'Weapon: {self.weapon.name}, {self.weapon.ammo}')
class Commander(Soldier):
    pass

class Unit:
    def __init__(self, unit_name: str, commander: Soldier, soldiers: list[Soldier], strike): #tank is an object from strike
        self.unit_name: str = unit_name
        self.commander: Soldier = commander
        self.soldiers: list[Soldier] = soldiers
        self.strike = strike


    def briefing(self):
        print(f'Unit Name: {self.unit_name}')
        self.commander.report()
        self.strike.strike() # this should be work in main file, this file does not recognize this class

    def mission(self, mission):
        print(f'-- {self.unit_name} --')
        for miss in mission:
            print(miss)

    def attack(self):
        rand = randint(0, 100)
        print(f'Attack: {rand} yard')
        if rand > 50:
            print("The attack was succeeded")
        else:
            print("The attack was failed")

class Infantry(Unit):
    def attack(self):
        print('Infantry attack')
        super().attack()


class Tank(StrikeOption, Unit):

    def attack(self):
        print(f'Tank attack')
        super().attack()

    def strike(self):
        self.ammo -= 1
        if self.ammo == 0:
            print("Out of ammo")
            return
        if self.s_range == 'short':
            print('strike short')
        elif self.s_range == 'medium':
            print('strike medium')
        elif self.s_range == 'long':
            print('strike long')

class Drone(StrikeOption, Unit):

    def attack(self):
        print('drone attack')
        super().attack()


    def strike(self):
        self.ammo -= 1
        if self.ammo == 0:
            print("Out of ammo")
            return
        if self.s_range == 'short':
            print('strike short')
        elif self.s_range == 'medium':
            print('strike medium')
        elif self.s_range == 'long':
            print('strike long')



class Sniper(Infantry):
    def attack(self):
        print('Sniper attack')
        super().attack()



class Army:
    total_attacks = 0
    def __init__(self, tank: Tank, drone: Drone, sniper: Sniper, infantry: Infantry):
        self.units = [tank, drone, sniper, infantry]
        self.attack_num = 0

    def attack_all(self):
        for attack in self.units:
            attack.attack()
            self.attack_num += 1

    def strongest_unit(self):
        max_soldiers = 0
        for unit in self.units:
            if len(unit.soldiers) > max_soldiers:
                max_soldiers = len(unit.soldiers)



# soldier3 = Soldier('Samuel', 'turai', weapon1)
# commander1 = Soldier('Libero', 'seren', weapon1)
# tank1 = Tank('3',3, 'long')
# a = Infantry('82', commander1, soldier3, tank1)
# print(a.attack())