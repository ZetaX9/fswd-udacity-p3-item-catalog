from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog_setup import Shop, Base, Product, User

engine = create_engine('sqlite:///shopproductwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='/static/blank_user.gif')
session.add(User1)
session.commit()

# Products for Urban Fruit
shop1 = Shop(user_id=1, name="Urban Fruit")

session.add(shop1)
session.commit()

product2 = Product(user_id=1, name="Tofu", description="Tofu",
                     price="$7.50", category="Produce", quantity="10", shop=shop1)

session.add(product2)
session.commit()


product1 = Product(user_id=1, name="French Fries", description="with garlic and parmesan",
                     price="$2.99", category="Confections", quantity="10", shop=shop1)

session.add(product1)
session.commit()

product2 = Product(user_id=1, name="Uncle Bob's Organic Dried Pears", description="Uncle Bob's Organic Dried Pears",
                     price="$5.50", category="Produce", quantity="10", shop=shop1)

session.add(product2)
session.commit()

product3 = Product(user_id=1, name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="$3.99", category="Condiments", quantity="10", shop=shop1)

session.add(product3)
session.commit()

product4 = Product(user_id=1, name="Sirloin Burger", description="Made with grade A beef",
                     price="$7.99", category="Beverages", quantity="10", shop=shop1)

session.add(product4)
session.commit()

product5 = Product(user_id=1, name="Root Beer", description="16oz of refreshing goodness",
                     price="$1.99", category="Beverage", quantity="10", shop=shop1)

session.add(product5)
session.commit()

product6 = Product(user_id=1, name="Iced Tea", description="with Lemon",
                     price="$.99", category="Beverage", quantity="10", shop=shop1)

session.add(product6)
session.commit()

product7 = Product(user_id=1, name="Grilled Cheese Sandwich",
                     description="On texas toast with American Cheese", price="$3.49", category="Beverages", shop=shop1)

session.add(product7)
session.commit()

product8 = Product(user_id=1, name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     price="$5.99", category="Beverages", shop=shop1)

session.add(product8)
session.commit()


# Products for Super Sundry
shop2 = Shop(user_id=1, name="Super Sundry")

session.add(shop2)
session.commit()


product1 = Product(user_id=1, name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     price="$7.99", category="Beverages", quantity="15", shop=shop2)

session.add(product1)
session.commit()

product2 = Product(user_id=1, name="Peking Duck",
                     description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", category="Beverages", quantity="15", shop=shop2)

session.add(product2)
session.commit()

product3 = Product(user_id=1, name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="$15", category="Beverages", quantity="15", shop=shop2)

session.add(product3)
session.commit()

product4 = Product(user_id=1, name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="$12", category="Beverages", quantity="15", shop=shop2)

session.add(product4)
session.commit()

product5 = Product(user_id=1, name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="$14", category="Beverages", quantity="15", shop=shop2)

session.add(product5)
session.commit()

product6 = Product(user_id=1, name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="$12", category="Beverages", quantity="15", shop=shop2)

session.add(product6)
session.commit()


# Product for Panda Garden
shop1 = Shop(user_id=1, name="Panda Garden")

session.add(shop1)
session.commit()


product1 = Product(user_id=1, name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     price="$8.99", category="Beverages", quantity="10", shop=shop1)

session.add(product1)
session.commit()

product2 = Product(user_id=1, name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     price="$6.99", category="Confections", quantity="10", shop=shop1)

session.add(product2)
session.commit()

product3 = Product(user_id=1, name="Gyoza", description="light seasoning of Japanese gyoza with salt and soy sauce, and in a thin gyoza wrapper",
                     price="$9.95", category="Beverages", quantity="10", shop=shop1)

session.add(product3)
session.commit()

product4 = Product(user_id=1, name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="$6.99", category="Beverages", quantity="10", shop=shop1)

session.add(product4)
session.commit()

product2 = Product(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", category="Beverages", quantity="10", shop=shop1)

session.add(product2)
session.commit()


# Product for Green Green
shop1 = Shop(user_id=1, name="Green Green")

session.add(shop1)
session.commit()


product1 = Product(user_id=1, name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="$2.99", category="Condiments", quantity="10", shop=shop1)

session.add(product1)
session.commit()

product2 = Product(user_id=1, name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="$5.99", category="Beverages", quantity="10", shop=shop1)

session.add(product2)
session.commit()

product3 = Product(user_id=1, name="Honey Boba Shaved Snow",
                     description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price="$4.50", category="Condiments", quantity="10", shop=shop1)

session.add(product3)
session.commit()

product4 = Product(user_id=1, name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="$6.95", category="Confections", quantity="10", shop=shop1)

session.add(product4)
session.commit()

product5 = Product(user_id=1, name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="$7.95", category="Beverages", quantity="10", shop=shop1)

session.add(product5)
session.commit()

product2 = Product(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$6.80", category="Beverages", quantity="10", shop=shop1)

session.add(product2)
session.commit()


# Product for Tony's Bistro
shop1 = Shop(user_id=1, name="Tony\'s Bistro ")

session.add(shop1)
session.commit()


product1 = Product(user_id=1, name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="$13.95", category="Beverages", quantity="10", shop=shop1)

session.add(product1)
session.commit()

product2 = Product(user_id=1, name="Chicken and Rice", description="Chicken... and rice",
                     price="$4.95", category="Beverages", quantity="10", shop=shop1)

session.add(product2)
session.commit()

product3 = Product(user_id=1, name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="$6.95", category="Beverages", quantity="10", shop=shop1)

session.add(product3)
session.commit()

product4 = Product(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", category="Condiments", quantity="10", shop=shop1)

session.add(product4)
session.commit()

product5 = Product(user_id=1, name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="$7.95", category="Beverages", quantity="10", shop=shop1)

session.add(product5)
session.commit()


# Product for Pesto
shop1 = Shop(user_id=1, name="Pesto")

session.add(shop1)
session.commit()


product1 = Product(user_id=1, name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="$9.95", category="Beverages", quantity="10", shop=shop1)

session.add(product1)
session.commit()

product2 = Product(user_id=1, name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="$7.95", category="Beverages", quantity="10", shop=shop1)

session.add(product2)
session.commit()

product3 = Product(user_id=1, name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="$6.50", category="Confections", quantity="10", shop=shop1)

session.add(product3)
session.commit()

product4 = Product(user_id=1, name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", category="Confections", quantity="10", shop=shop1)

session.add(product4)
session.commit()

product2 = Product(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.00", category="Beverages", quantity="10", shop=shop1)

session.add(product2)
session.commit()


# Menu for Auntie Lim Grocery
shop1 = Shop(user_id=1, name="Auntie Lim Grocery")

session.add(shop1)
session.commit()

product9 = Product(user_id=1, name="Chicken Fried Steak",
                     description="Fresh battered sirloin steak fried and smothered with cream gravy", price="$8.99", category="Beverages", quantity="10", shop=shop1)

session.add(product9)
session.commit()


product1 = Product(user_id=1, name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="$2.99", category="Condiments", quantity="10", shop=shop1)

session.add(product1)
session.commit()

product2 = Product(user_id=1, name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="$10.95", category="Beverages", quantity="10", shop=shop1)

session.add(product2)
session.commit()

product3 = Product(user_id=1, name="Morels on toast (seasonal)",
                     description="Wild morel mushrooms fried in butter, served on herbed toast slices", price="$7.50", category="Confections", quantity="10", shop=shop1)

session.add(product3)
session.commit()

product4 = Product(user_id=1, name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="$8.95", category="Beverages", quantity="10", shop=shop1)

session.add(product4)
session.commit()

product2 = Product(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", category="Beverages", quantity="10", shop=shop1)

session.add(product2)
session.commit()

product10 = Product(user_id=1, name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="$1.99", category="Condiments", quantity="10", shop=shop1)

session.add(product10)
session.commit()


# Product for Cocina Y Amor
shop1 = Shop(user_id=1, name="Cocina Y Amor ")

session.add(shop1)
session.commit()


product1 = Product(user_id=1, name="Super Burrito Al Pastor",
                     description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", price="$5.95", category="Beverages", quantity="10", shop=shop1)

session.add(product1)
session.commit()

product2 = Product(user_id=1, name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="$7.99", category="Beverages", quantity="10", shop=shop1)

session.add(product2)
session.commit()


shop1 = Shop(user_id=1, name="State Bird Provisions")
session.add(shop1)
session.commit()

product1 = Product(user_id=1, name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="$5.95", category="Confections", quantity="10", shop=shop1)

session.add(product1)
session.commit

product1 = Product(user_id=1, name="Guanciale Chawanmushi",
                     description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)", price="$6.95", category="Condiments", quantity="10", shop=shop1)

session.add(product1)
session.commit()


product1 = Product(user_id=1, name="Lemon Curd Ice Cream Sandwich",
                     description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews", price="$4.25", category="Condiments", quantity="10", shop=shop1)

session.add(product1)
session.commit()


print "added products!"
