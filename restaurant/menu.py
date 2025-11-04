# from menu_items import MenuItem

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item: str) -> None:
        self.items.append(menu_item)

    def remove_item(self, item_name: str) -> None:
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)

    def get_item_by_name(self, name: str):
        for item in self.items:
            if item.name == name:
                return item

        return 'This item is not exists.'

    def get_item_by_category(self, category):
        for item in self.items:
            if item.category == category:
                return item

        return 'This item is not exists.'

    def display_menu(self):
        for item in self.items:
            print(f''
             f'Name: {item.name}\n'
             f'Price: {item.price}\n'
             f'Category {item.category}\n'
             f'Is available: {item.available}\n'
             f'----------')

    def get_total_items(self):
        return len(self.items)

