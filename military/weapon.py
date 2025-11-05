class Weapon:
    total_weapons: int = 0
    def __init__(self, name: str, ammo: int):
        self.name: str = name
        self.ammo: int = ammo
        Weapon.total_weapons += 1


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


