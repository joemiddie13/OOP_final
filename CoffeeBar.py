class CoffeeBar:
    def __init__(self, name, barista=None):
        """
        Initializes the CoffeeBar with essential attributes.
        - name: Name of the coffee bar
        - barista: The barista serving at the coffee bar (optional)
        - orders_list: List to keep track of pending orders
        - register: Tracks total revenue from orders
        - tip_jar: Accumulates tips from customers
        - receipts: Stores details of completed orders
        """
        self.name = name
        self.orders_list = []
        self.barista = barista
        self.register = 0.0
        self.tip_jar = 0.0
        self.receipts = []

    def place_order(self, order):
        """
        Adds a new order to the pending orders list.
        """
        self.orders_list.append(order)

    def process_orders(self):
        """
        Processes each pending order by:
        - Performing financial transactions
        - Displaying order details with a barista greeting (if barista is present)
        - Moving processed orders to the receipts list
        - Clears the pending orders list after processing
        """
        for order in self.orders_list:
            order.person.wallet -= (order.price + order.tip)
            self.register += order.price
            self.tip_jar += order.tip

            greeting = f"{self.barista.greeting}" if self.barista else ""
            print(f"{greeting} {order.to_string()}")

            self.receipts.append(order)

        self.orders_list = []
  
    def cash_out(self):
        """
        Displays the total revenue in the register when cashing out.
        """
        print(f"Total amount in register: ${self.register: .2f}")