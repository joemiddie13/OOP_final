from Person import Person
from CoffeeBar import CoffeeBar
from Barista import Barista

# Welcome to Rocko Brewing, the only coffee shop in town where you might hear a good dog joke while enjoying your drink.

# Amy, a software engineer who loves puns almost as much as her coffee, enters with her Dalmatian, Spot.
amy = Person("Amy", "Coffee", 100.0)

# She jokes, "What do you call a cold dog? A Chilli Dog!" Spot wags his tail in agreement.

# Next is Bob, a teacher with a fondness for tea and bad jokes. He's accompanied by his Beagle, Sherlock.
bob = Person("Bob", "Tea", 100.0)

# As Bob orders, he chuckles, "What kind of dog does Dracula have? A bloodhound!"

# Cat, a veterinarian, walks in with her Husky, Frost. She's known for her love of milk and witty humor.
cat = Person("Cat", "Milk", 100.0)

# While ordering, she smiles and says, "Why did the poor dog chase his own tail? He was trying to make both ends meet!"

# Behind the counter is Kevin, the barista, known for his espresso skills and his Pug, Bean.
kevin = Barista("Kevin", "Espresso", "Hey dude!", 200.0)

# Kevin greets each customer with his signature line and a new dog joke: "What do you call a dog magician? A labracadabrador!"

coffee_bar = CoffeeBar("Rocko Brewing", kevin)

# Today's special at Rocko Brewing: 'Pawspresso' for humans and 'Woof-fee' for their furry friends.
drink_prices = {"Coffee": 5.0, "Tea": 3.0, "Milk": 2.0}

# Amy orders her coffee and tips 20%. Spot seems to approve of her generosity.
coffee_bar.place_order(amy.my_order(drink_prices[amy.favorite_drink], 20))

# Bob orders his tea, leaving an 18% tip. Sherlock howls softly, as if to say "well done".
coffee_bar.place_order(bob.my_order(drink_prices[bob.favorite_drink], 18))

# Cat goes for her milk, tipping 15%. Frost gives a happy bark, echoing the friendly atmosphere.
coffee_bar.place_order(cat.my_order(drink_prices[cat.favorite_drink], 15))

# Kevin processes the orders with his usual flair, making each customer feel special. Bean the Pug watches on proudly.
coffee_bar.process_orders()

# At the end of this fun and furry round of orders, Kevin cashes out the register.
coffee_bar.cash_out()

# The tips, well-earned from a day filled with laughter and wagging tails, are added to Kevin's wallet.
kevin.wallet += coffee_bar.tip_jar

# As the day winds down at Rocko Brewing, everyone leaves with a smile, two-legged and four-legged customers alike.