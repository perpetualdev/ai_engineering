# Ask user to enter 5 favorite fruits
fav_fruits = set()
for i in range(1, 6):
  fruit = input(f"Favorite fruit {i}: ")
  fav_fruits.add(fruit)

# Display them
print("Favourite Fruits: ", fav_fruits)
