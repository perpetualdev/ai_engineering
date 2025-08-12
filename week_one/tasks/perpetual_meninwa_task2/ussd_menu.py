# Design a mock USSD interface for a mobile service.
#  1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
print("Welcome to the MTN Service...")

#  2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
ussd_code = input("Dial *345# to continue: ")

#  3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
print("1. Check Balance")
print("2. Buy Airtime")
print("3. Buy Data")

#  4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
option = input("Please select an option from above: ")

#  5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
print(f"You selected option {option}.")

#  6. Ask for an amount (if applicable) and store it as a number using type casting.
amount = input("How much airtime or data would you like to buy? ")

#  7. Display a final message summarizing the transaction.
print(f"Your transaction is successful... 🎉🎉. You have purchased data/airtime of {amount}. Thank you for choosing MTN")