# Ask for festival name, location and month held 
festival_name = input("What is the Festival Name? ")
festival_location = input("What is the Location of the festival? ")
month_held = input("What month is the festival holding? ")

# Display the info with quotes around the festival name using escape sequence
print(f"\"{festival_name}\" festival will be holding at {festival_location} in {month_held}.")