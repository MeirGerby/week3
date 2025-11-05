import weapon
class Agent:
    def __init__(self, code_name: str, clearance_level: int):
        self.code_name: str = code_name
        self.clearance_level: int = clearance_level

class Mission:
    def __init__(self, mission_name: str, target: str, assigned_agent: Agent, weapon):
        self.mission_name: str = mission_name
        self.target: str = target
        self.assigned_agent: Agent = assigned_agent
        self.weapon = weapon
    def __str__(self):
        return (f'--Mission--'
                f'Name: {self.mission_name}'
                f'Target: {self.target}')

    def briefing(self):
        print(f'--mission--'
              f'name: {self.mission_name}'
              f'Target: {self.target}'
              f'Agent CodeName: {self.assigned_agent.code_name}')

    def execute(self):
        print('Error: execute is not available')



    def strike(self):
        print('Error: strike is not available')

    def attack(self):
        print('Error: attack is not available')


class ReconMission(Mission):

    def execute(self):
        self.weapon.ammo -= 1
        print('ReconMission: execute')


class StrikeMission(Mission):
    def execute(self):
        self.weapon.ammo -= 1
        print('StrikeMission: execute')

    def strike(self):
        self.weapon.ammo -= 1
        print('StrikeMission: strike')

class RescueMission(Mission):

    def execute(self):
        self.weapon.ammo -= 1
        print('RescueMission: execute')


    def attack(self):
        self.weapon.ammo -= 1
        print('RescueMission: attack')


    def strike(self):
        self.weapon.ammo -= 1
        print('RescueMission: strike')



class MissionManager:
    def __init__(self):
        self.missions = []




    def add(self, mission):
        allowed_level = 3
        if mission.clearance_level > allowed_level:
            return
        self.missions.append(mission)

    def find_by_agent(self, codename):
        for mission in self.missions:
            if mission.codename == codename:
                print(mission)

    def remove(self, mission):
        for m in self.missions:
            if m.mission_name == mission.mission_name:
                self.missions.remove(mission)


weapon1 = weapon.Weapon('M16', 90)
weapon2 = weapon.Weapon('usi', 900)
soldier1 = weapon.Soldier('Meir', 'samal', weapon1)
soldier2 = weapon.Soldier('David', 'turai', weapon2)
soldier3 = weapon.Soldier('Samuel', 'turai', weapon1)
commander = weapon.Soldier('Libero', 'seren', weapon1)
soldiers = [soldier1, soldier2, soldier3]
tank = weapon.Tank('mercava3', 300)
drone = weapon.Drone('F-16', 34)
unit1 = weapon.Unit("8200", commander, soldiers, [tank, drone])

for strike in unit1.strike:
    strike.strike()
agent1 = Agent('Meir', 2)
agent2 = Agent('David', 2)
mission1 = Mission('am celavi','Iran', agent1)
mission2 = Mission('zuck aitan','gaza', agent2)
mission_manager = MissionManager()
mission_manager.add(mission1)
mission_manager.add(mission2)

# k = mission_manager.remove(d)
# print(k)

recon_mission = ReconMission('recon', 'gaza', agent1)
rescue_mission = RescueMission('rescue', 'iran', agent2)
mission_manager.add(recon_mission)
mission_manager.add(rescue_mission)
print(mission_manager.missions)