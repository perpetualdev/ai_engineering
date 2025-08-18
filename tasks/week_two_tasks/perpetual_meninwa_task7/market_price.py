# store items and their market prices in a dictionary
market_items = []
market_prices = {}
for i in range(1, 3):
  item = input(f"Enter item {i} name: ")
  market_items.append(item)
  market_prices[item] = float(input(f"Enter the price for {item}: "))
print(market_items)
print(market_prices)

for item in market_prices:
  check_if_update = input(f"Do you want to update the price for {item}? (yes/no): ").strip().lower()
  if check_if_update == 'yes':
    new_price = float(input(f"Enter the new price for {item}: "))
    market_prices.update({item: new_price})
    print(market_prices)
  else:
    continue

print("Market Items: ", market_prices.keys())
print("Market Prices: ", market_prices.values())
# Display the items and their prices
for item, price in market_prices.items():
  print(f"{item}: ${price}")