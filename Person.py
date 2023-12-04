from Order import Order

class Person:
    """
    The Person class represents an individual who can place orders at the coffee bar.
    It includes their name, favorite drink, and the amount of money in their wallet.
    """

    def __init__(self, name, favorite_drink, wallet_amount):
        """
        Initializes a Person instance.

        Parameters:
        - name: The name of the person
        - favorite_drink: The person's favorite drink
        - wallet_amount: The amount of money the person has in their wallet

        This method sets up the basic attributes for a person visiting the coffee bar.
        """
        self.name = name  # The person's name
        self.favorite_drink = favorite_drink  # The person's favorite drink
        self.wallet = wallet_amount  # The amount of money in the person's wallet

    def my_order(self, price, tip_percentage):
        """
        Creates an order for the person's favorite drink.

        Parameters:
        - price: The price of the drink
        - tip_percentage: The percentage of the price that will be given as a tip

        Returns:
        An Order object representing the person's order, including the cost and the tip.

        This method calculates the tip based on the price and tip percentage, and then
        creates an order with these details.
        """
        tip_amount = price * (tip_percentage / 100)  # Calculate the tip amount
        return Order(self, self.favorite_drink, price, tip_amount)  # Create and return an order