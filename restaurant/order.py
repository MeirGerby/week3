class Order:
    def __init__(self, customer, order_number):
        self.customer = customer
        # the customer is an object made of customer class
        self.order_number = order_number
        self.items = []
        self.status = 'pending'
        self.total_price = 0

    def add_item(self, menu_item):
        self.items.append(menu_item)
        self.total_price += menu_item.price

    def remove_item(self, menu_item):
        self.items.remove(menu_item)
        self.total_price -= menu_item.price

    def get_total(self):
        return self.total_price

    def get_status(self, new_status):
        if new_status == 'pending':
            self.status = 'pending'
        elif new_status == 'cooking':
            self.status = 'cooking'
        elif new_status == 'ready':
            self.status = 'ready'
        elif new_status == 'delivered':
            self.status = 'delivered'

    def display_order(self):
        print(f'order number: {self.order_number}\n'
              f'Costumer: {self.customer}\n'
              f'Items: {self.items}'
              f'Total: {self.total_price}'
              f'Status: {self.status}')

    def is_complete(self):
        if self.status == 'delivered':
            return True
        else:
            return False