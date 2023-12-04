from Person import Person
from Order import Order
from CoffeeBar import CoffeeBar
from Barista import Barista

# Create 3 instances of customers
amy = Person("Amy", "Coffee")
bob = Person("Bob", "Tea")
cat = Person("Cat", "Milk")

# Create an instance of CoffeeBar
coffee_bar = CoffeeBar("Rocko Brewing")

# Place orders
coffee_bar.place_order(amy.my_order())
coffee_bar.place_order(bob.my_order())
coffee_bar.place_order(cat.my_order())

# Process orders
coffee_bar.process_orders()

# Instance of Barista, Kevin
kevin = Barista("Kevin", "Espresso", "Hey dude!")

# Instance of CoffeeBar with Kevin as the barista
coffee_bar = CoffeeBar("Rocko Brewing", kevin)

# Place orders
coffee_bar.place_order(amy.my_order())
coffee_bar.place_order(bob.my_order())
coffee_bar.place_order(cat.my_order())

# Process orders
coffee_bar.process_orders()