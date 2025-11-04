class Customer:
    def __init__(self, name):
        self.name = name
        self.satisfaction = 50

    def increase_satisfaction(self, amount):
        self.satisfaction += amount
        if self.satisfaction > 100:
            return 100
        else:
            return self.satisfaction

    def decrease_satisfaction(self, amount):
        self.satisfaction -= amount
        if self.satisfaction < 0:
            return 0
        else:
            return self.satisfaction

    def is_happy(self):
        if self.satisfaction > 70:
            return True
        else:
            return False

    def get_info(self):
        return (f'Name: {self.name},\n'
                f'Satisfaction Level: {self.satisfaction}')


