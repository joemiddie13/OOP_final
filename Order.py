class Order:
    """
    The Order class represents an order placed in the coffee bar.
    It includes details about the person placing the order, the type of drink,
    its price, and the tip given.
    """

    def __init__(self, person, drink_type, price, tip):
        """
        Initializes an Order instance.

        Parameters:
        - person: The Person object who is placing the order
        - drink_type: Type of drink being ordered (e.g., 'Coffee', 'Tea')
        - price: The cost of the drink
        - tip: The tip amount given by the customer

        Each order associates a customer with a drink, including the financial details
        of the transaction (price and tip).
        """
        self.person = person        # The customer who placed the order
        self.drink_type = drink_type  # The type of drink ordered
        self.price = price          # The price of the drink
        self.tip = tip              # The tip given by the customer

    def to_string(self):
        """
        Returns a string representation of the order.

        The method creates a formatted string that includes the name of the person
        and the type of drink they ordered. This is useful for displaying the order
        details in a user-friendly format.
        
        Returns:
        A string in the format: "{Person's name} orders: {Drink type}"
        """
        return f"{self.person.name} orders: {self.drink_type}"