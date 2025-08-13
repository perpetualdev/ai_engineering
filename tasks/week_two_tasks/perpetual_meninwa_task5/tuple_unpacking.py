# Ask user for their first name, age, favorite color, home town 
first_name = input("What is your first name?: ")
age = input("What is your age?: ")
fav_color = input("What is your favorite color?: ")
home_town = input("What is your home town?: ")

# and store then in a tuple
user_details = (first_name, age, fav_color, home_town)

# Unpack tuple
name, user_age, favorite_color, hometown = user_details
print(name)
print(user_age)
print(favorite_color)
print(hometown)

# Use escape sequence to align each piece of information nicely
print(f"Name\t\tAge\tFavourite Color\t\tHome Town\n=================================================================\n{name}\t{user_age}\t{favorite_color}\t\t\t{hometown}")
