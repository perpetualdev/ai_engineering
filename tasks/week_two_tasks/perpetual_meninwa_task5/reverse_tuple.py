# Ask user for five best friends' names
# Create a new list to store the friends' names
friends_list = []

# Append the friends' names
friend_one = input("Best friend one: ")
friends_list.append(friend_one)
friend_two = input("Best friend two: ")
friends_list.append(friend_two)
friend_three = input("Best friend three: ")
friends_list.append(friend_three)
friend_four = input("Best friend four: ")
friends_list.append(friend_four)
friend_five = input("Best friend five: ")
friends_list.append(friend_five)

# Convert list to tuple
friends = tuple(friends_list)
# print(friends)

# Print the friends in reverse order
print(friends[::-1])

# ========================= OR =============================

# Ask user for five best friends' names (separated by space)
friend_list_items = input("Enter your best friends' names separated by space: ")

# Use the split method to put them in a list and tuple constructor to convert to tuple
friends_too = tuple(friend_list_items.split(" "))

# print(friends_too)

# Reverse the tuple
print(friends_too[::-1])
