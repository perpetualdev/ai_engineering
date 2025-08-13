# Ask user to enter 5 favorite fruits
fruit1 = input("Favorite fruit one: ")
fruit2 = input("Favorite fruit two: ")
fruit3 = input("Favorite fruit three: ")

# Store them in a set
fav_fruits = {fruit1, fruit2, fruit3}

# Display them
print("Favourite Fruits: ", fav_fruits)

# ====================== OR ===============
fav_fruits_too = set()
fruit_one = input("Favorite fruit one: ")
fav_fruits_too.add(fruit_one)
fruit_two = input("Favorite fruit two: ")
fav_fruits_too.add(fruit_two)
fruit_three = input("Favorite fruit three: ")
fav_fruits_too.add(fruit_three)
print("Second Favorite Fruits: ", fav_fruits_too)
