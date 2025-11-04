class IDrive:
    @staticmethod
    def drive():
        print('I can drive')

class IFly:
    @staticmethod
    def fly():
        print('I can fly')

class ISail:
    @staticmethod
    def sail():
        print('I can sail')

class Tank:
    def __init__(self, drive):
        self.drive = drive



class FighterJet:
    def __init__(self, fly, drive):
        self.fly = fly
        self.drive = drive

class Submarine:
    def __init__(self, sail):
        self.sail = sail

tank = Tank(IDrive())
fighter_jet = FighterJet(IFly(), IDrive())
submarine = Submarine(ISail())
tank.drive.drive()
fighter_jet.drive.drive()
fighter_jet.fly.fly()
submarine.sail.sail()