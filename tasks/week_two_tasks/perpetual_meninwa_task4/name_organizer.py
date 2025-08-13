# Ask user to enter 5 names(separated by spaces)
five_names = input("Please enter five names separated by spaces: ")
# Convert names to lowercase
split_names = five_names.lower().split(" ")
# Sort list alphabetically
split_names.sort()
print(split_names)
# Display name one name per line
[print(f"{name}") for name in split_names]
