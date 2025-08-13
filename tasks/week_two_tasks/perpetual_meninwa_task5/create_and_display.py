# Ask the user to enter 3 fav dishes (one at a time)
# Store them in a tuple called dishes
dish_one = input("Favorite dish 1: ")
dish_two = input("Favorite dish 2: ")
dish_three = input("Favorite dish 3: ")

# Print the tuple in a single line, separating items with commas
dishes = (dish_one, dish_two, dish_three)
print("Tuple Dishes: ", dishes)

# Use the \n escape sequence to print each dish on a new line
print(f"{dish_one}\n{dish_two}\n{dish_three}")
