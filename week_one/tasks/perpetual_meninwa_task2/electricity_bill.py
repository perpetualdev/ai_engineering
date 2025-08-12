# Ask the user for fullname, units consumed in kWh and cost per unit
customer_name = input("Full Name: ")
units_consumed = int(input("Units Consumed: "))
cost_per_unit = float(input("Cost Per Unit: "))

# Calculate total bill
total_bill = cost_per_unit * units_consumed

# Print in a neatly formatted receipt using escape sequence
print(f"Customer Name\t\tUnits Consumed\tCost Per Unit\tTotal\n==================================================================\n{customer_name}\t\t{units_consumed}\t\t{cost_per_unit:,.2f}\t\t{total_bill:,.2f}")
