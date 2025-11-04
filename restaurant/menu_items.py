class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.available = True

    def get_info(self):
        return (f'Name: {self.name}\n'
                f'Price: {self.price}\n'
                f'Category {self.category}\n'
                f'----------')

    def set_available(self):
        if self.available is True:
            self.available = False

        else:
            self.available = True

    def is_available(self):
        return f'Available: {self.available}'

