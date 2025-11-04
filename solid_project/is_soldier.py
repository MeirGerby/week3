

class Shoot:

    @staticmethod
    def shoot():
        print('shoot')

class Navigate:

    @staticmethod
    def navigate():
        print('navigate')

class CallAirSupport:

    @staticmethod
    def call_air_support():
        print('call the air support')

class Infantry:

    def __init__(self, shoot, navigate):
        self.shoot = shoot
        self.navigate = navigate

    def display(self):
        print(f'shoot: {self.shoot},navigate: {self.navigate}')


class ForwardObserver:
    def __init__(self, shoot, call_air_support):
        self.shoot = shoot
        self.call_air_support = call_air_support

    def display(self):
        print(f'shoot: {self.shoot}, support:{self.call_air_support}')

class Pilot:
    def __init__(self, call_air_support):
        self.call_air_support = call_air_support

    def display(self):
        print(f'support: {self.call_air_support}')