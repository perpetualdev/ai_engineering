# ===================== TUPLES ========================
# Creating Tuples
# Parentheses()
fruits = ("apples", "banana", "cherry")
print(fruits) # ('apples', 'banana', 'cherry')

# Without parentheses(tuple packing)
numbers = 1, 2, 3
print(numbers) # (1, 2, 3)

# Single-item tuple (must include a comma)
single_item = ("apple",) 
# without comma, it is a str type 
# apple
# <class 'str'>
print(single_item) # ('apple',)
print(type(single_item)) # <class 'tuple'>

# Using tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)  # ('apple', 'banana', 'cherry')

# ===================== CHAR OF TUPLES ======================
# Ordered
colors = ("red", "green", "blue")
print(colors[0])   # red

# Immutable - cannot change after creation
# colors[1] = "yellow"
# TypeError: 'tuple' object does not support item assignment

# Allows duplicates
numbers = (1, 2, 2, 3)
print(numbers)   # (1, 2, 2, 3)

# Nested tuples
nested = (("a", "b"), (1, 2))
print(nested) # (('a', 'b'), (1, 2))

# =================== TUPLE OPERATIONS ======================
# Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])   # banana
print(fruits[-1])  # cherry

# Slicing
print(fruits[0:2])   # ('apple', 'banana')
print(fruits[::-1])  # ('cherry', 'banana', 'apple')

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)   # (1, 2, 3, 4)

# Repetition
nums = (1, 2)
print(nums * 3)   # (1, 2, 1, 2, 1, 2)

# Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)      # True
print("grape" not in fruits)   # True

# Iteration
for fruit in fruits:
  print(fruit)
# apple
# banana
# cherry

# You can’t modify a tuple directly, but you can

#    - Convert it to a list, modify it, then convert back.

#    - Use built-in functions to work with tuple contents.
fruit_list = list(fruits)
fruits_list.append("grape")
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# ===================== UNPACKING TUPLES ========================
person = ("John", 25, "Nigeria")
name, age, country = person
print(name)      # John
print(age)       # 25
print(country)   # Nigeria

# Tuple Methods
# count()
numbers = (1, 2, 2, 3, 4)
print(numbers.count(2))   # 2 (the number of occurrences)
# index()
print(numbers.index(3))   # 3 (position of the first occurrence of 3)

# Built-in Functions with Tuples
nums = (4, 1, 7, 3)

print(len(nums))  # the number of items in the tuple (4)
print(max(nums))  # the highest number in the tuple (7)
print(min(nums))  # the lowest number in the tuple (1)
print(sum(nums))  # the sum of the numbers in the tuple (15)
