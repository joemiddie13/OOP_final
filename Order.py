class Order:
  def __init__(self, person, drink_type):
    self.person = person
    self.drink_type = drink_type
  
  def to_string(self):
    return f"{self.person.name} orders: {self.drink_type}"