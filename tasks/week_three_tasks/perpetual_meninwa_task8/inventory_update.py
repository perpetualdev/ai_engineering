store = {"Book": 10, "Pen": 20, "Bag": 5}

# Ask the user to input the item they want to buy
item = input("Select item you would like to buy: ")

if item in store:
# Ask the user to input the qty of the item they want to buy
  qty = int(input("How many would you like to buy? "))
  print(f"Before purchase: {store}")
# Use the assignment operator to update the item qty
  store[item] -= qty
  print(f"After purchase: {store}")
else:
  print(f"Item {item} does not exist in the store!")

