class CoffeeBar:
  def __init__(self, name):
    self.name = name
    self.orders_list = []
  
  def place_order(self, order):
    self.orders_list.append(order)

  def process_orders(self):
    for order in self.orders_list:
      print(order.to_string())