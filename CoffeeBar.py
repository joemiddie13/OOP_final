class CoffeeBar:
    def __init__(self, name, barista=None):
        self.name = name
        self.orders_list = []
        self.barista = barista

    def place_order(self, order):
        self.orders_list.append(order)

    def process_orders(self):
        if self.barista is not None:
            greeting = self.barista.greeting
        else:
            greeting = ""
        for order in self.orders_list:
            print(f"{greeting} {order.to_string()}")