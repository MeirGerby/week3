# import weapon, mission_briefing as mission
from abc import abstractmethod

class StrikeOption:
    def __init__(self, name: str, ammo: int, s_range: str):
        self.name: str = name
        self.ammo: int = ammo
        self.s_range: str = s_range

    def strike(self):
        self.ammo -= 1
        if self.ammo == 0:
            print('Error: there is no more ammo')







# weapon1 = weapon.Weapon('M16', 90)
# weapon2 = weapon.Weapon('usi', 900)
# soldier1 = weapon.Soldier('Meir', 'samal', weapon1)
# soldier2 = weapon.Soldier('David', 'turai', weapon2)
# soldier3 = weapon.Soldier('Samuel', 'turai', weapon1)
# commander = weapon.Soldier('Libero', 'seren', weapon1)
# soldiers = [soldier1, soldier2, soldier3]
# tank = Tank('mercava3', 300)
# drone = Drone('F-16', 34)
# unit1 = weapon.Unit("8200", commander, soldiers, [tank, drone])

# for strike in unit1.strike:
#     strike.strike()


# agent1 = mission.Agent('Meir', 2)
# agent2 = mission.Agent('David', 2)
# mission1 = mission.Mission('am celavi','Iran', agent1)
# mission2 = mission.Mission('zuck aitan','gaza', agent2)
# mission_manager = mission.MissionManager()
# add_mission1 = mission_manager.add(mission1)
# add_mission2 = mission_manager.add(mission2)
#
# k = mission_manager.remove(d)
# print(k)












