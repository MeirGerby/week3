class Order:
    def __init__(self, items: list[str], total_price: float):
        self.items: list[str] = items
        self.total_price: float = total_price


class InvoicePrinter:

    @staticmethod
    def print_invoice(order: Order):
        for item in order.items:
            print(f'Item: {item}')
        print(f'Total price: {order.total_price}')

InvoicePrinter.print_invoice(Order(['Apples', 'Bananas'], 52.4))
