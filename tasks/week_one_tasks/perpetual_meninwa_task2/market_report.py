# Ask user to input market name, number of traders and daily revenue
market_name = input("Market Name: ")
num_of_traders = int(input("Number of Traders: "))
daily_revenue = float(input("Daily Revenue: "))

# Calculate total revenue
total_revenue = num_of_traders * daily_revenue

# Print Market Report with f-string formatting with commas
print(f"Total Revenue for {market_name} is {total_revenue:,.2f}")