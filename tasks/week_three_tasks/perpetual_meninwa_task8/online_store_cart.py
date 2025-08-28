# Defining variables
items = ['Book', 'Pen', 'Bag']
prices = [1200, 550, 2500]
cart_total = 0

# using dict zip attach item to prices
items_prices = dict(zip(items, prices))
print(items_prices)

# Create an empty array
user_items = []

# Get the item added to cart
item1 = input("Enter item to add to cart: ")
# Add the price of the item 1
if item1 in items:
  cart_total += items_prices[item1]
  user_items.append(item1)
else:
  print(f"{item1} does not exist in the store!")

item2 = input("Enter item to add to cart: ")
# Add the price of the second item
if item2 in items:
  cart_total += items_prices[item2] 
  user_items.append(item2)
else:
  print(f"{item1} does not exist in the store!")


# Print the list of items and the total price using an f-string 
print(f"\nItems: {user_items}\nTotal Price: N{cart_total}")
