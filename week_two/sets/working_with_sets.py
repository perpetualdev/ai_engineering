# ============================ SETS ================================
# Creating Sets
# Using curly braces
fruits = {"apple", "banana", "mango"}
print(fruits) 
# {'mango', 'banana', 'apple'}

# Using the set() constructor
numbers = set([1, 2, 3, 4])
print(numbers)
# {1, 2, 3, 4}

# Creating empty set (must use set(), not {})
empty_set = set()
print(empty_set)
# set()

# From a string (duplicates removed automatically)
letters = set("mississippi")
print(letters)
# {'s', 'p', 'm', 'i'}

# SET OPERATIONS
# Adding
colors = {"red", "blue"}
colors.add("green")
print(colors)
# {'green', 'red', 'blue'}

# Removing
colors.remove("blue")  # Removes item, raises error if not found
print(colors) 
# colors.remove("nude") # KeyError: 'nude'
colors.discard("yellow")  # Removes if found, no error if missing 
print(colors)

# Pop
colors = {"red", "blue", "green"}
removed = colors.pop()
print("Removed: ", removed)
# Removed:  red

# Clear set
colors.clear()
print(colors)
# set()

# =================== MATHEMATICAL SET OPERATIONS ==========================
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1 | set2)
# {1, 2, 3, 4, 5, 6}
print(set1.union(set2))
# {1, 2, 3, 4, 5, 6}

# Intersection
print(set1 & set2) # {3, 4}
print(set1.intersection(set2)) # {3, 4}

# Difference
print(set1 - set2) # Meaning what is included in set1 that is not included in set2
print(set1.difference(set2))
# {1, 2}

# Symmetric Difference
print(set1 ^ set2)  # Exclude what is included in both sets
print(set1.symmetric_difference(set2))
# {1, 2, 5, 6}

# ================= WORKING WITH SETS ===============================
# Collecting unique visitors to an event
visitors = set()

# Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu")  # Duplicate, ignored automatically
print("Visitors: ", visitors)

# Checking if a visitor attended

name = "Aisha"
if name in visitors:
  print(f"{name} attended the event.")
else:
  print(f"{name} did not attend the event.")
