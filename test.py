from Person import Person

# Person instances
person1 = Person("Alice", "Coffee")
person2 = Person("Bob", "Tea")

# Generate orders
order1 = person1.my_order()
order2 = person2.my_order()

# Print order details
print(order1.to_string())
print(order2.to_string())
