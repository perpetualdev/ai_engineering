# ask user for amount in naira (float), exchange rate in US Dollars (float) and exchange rate in pounds (float)
amount = float(input("Amount: "))
exchange_in_usd = float(input("Exchange Rate in US Dollars: "))/amount
exchange_in_pounds = float(input("Exchange Rate in Pounds: "))/amount

# Convert and print results with thousands separators and currency symbols, neatly aligned in a table-like format using escape sequences.
print(f"Amount\t\tEX($)\t\tEX()\n=======================================\n{amount}\t\t${exchange_in_usd:.2f}\t\t{exchange_in_pounds:.2f}")
