# Ask user to enter 3 items for shopping list
list_one = input("Enter first shopping item: ")
list_two = input("Enter second shopping item: ")
list_three = input("Enter third shopping item: ")

shopping_items = (list_one, list_two, list_three)
print("Tuple Shopping Items: ", shopping_items)

# Convert to a list
shopping_list = list(shopping_items)
print("Shopping Items in a List: ", shopping_list)

# Ask for two more items to add
list_four = input("Enter fourth shopping item: ")
shopping_list.append(list_four)
list_five = input("Enter fifth shopping item: ")
shopping_list.append(list_five)
print("Appended Shopping List: ", shopping_list)

# Convert back to tuple using the tuple constructor
shopping_tuple = tuple(shopping_list)
print("List converted to tuple after appending: ", shopping_tuple)

# print updated list using join separated by " | "
print(" | ".join(shopping_list))
