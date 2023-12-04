from Order import Order

class Person:
  def __init__ (self, name, favorite_drink):
    self.name = name
    self.favorite_drink = favorite_drink

  def my_order(self):
    return Order(self, self.favorite_drink)