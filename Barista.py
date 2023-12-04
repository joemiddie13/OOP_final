from Person import Person

class Barista(Person):
    """
    The Barista class represents a barista in the coffee bar.
    It inherits from the Person class and adds a unique greeting attribute.
    """

    def __init__(self, name, favorite_drink, greeting, wallet_amount):
        """
        Initializes a Barista instance.
        
        Parameters:
        - name: Name of the barista
        - favorite_drink: The barista's favorite drink
        - greeting: A special greeting that the barista uses
        - wallet_amount: The initial amount in the barista's wallet

        The Barista class extends the Person class, utilizing its initialization
        to set up common attributes, and adds a specific attribute for the barista's greeting.
        """
        # Call to the superclass (Person) initializer
        super().__init__(name, favorite_drink, wallet_amount)
        self.greeting = greeting  # Unique greeting for the barista