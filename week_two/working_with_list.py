# =========== METHODS TO CREATE LIST ============
# Using square brackets
empty_list = []
print(empty_list)  # Output: []

# Using list() constructor
empty_list2 = list()
print(empty_list2) # Output: []

# List with elements
# Integers
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Output: [1, 2, 3, 4, 5]

# Strings
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Mixed
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list) # Output: ['Alice', 25, 5.8, True]

# You can convert strings, tuple or other iterables into a list
# Strings to List
chars = list("hello")
print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']

# Tuple to List
my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)   # Output: [10, 20, 30]

# Range to List
numbers_range = list(range(5))
print(numbers_range)  # Output: [0, 1, 2, 3, 4]

# LIST COMPREHENSION
# Squares of numbers 0 - 4
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Even numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)

# Creating Nested List
# Matrix-like list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)  # Output: [[1, 2], [3, 4], [5, 6]]

# Access elements in nested list
print(matrix[0])      # Output: [1, 2]
print(matrix[0][1])   # Output: 2

# ============== CHARS OF A LIST ================
# Ordered Collection
fruits = ["mango", "orange", "banana"]
print(fruits)     # ['mango', 'orange', 'banana']
print(fruits[0])  # mango (first element)
print(fruits[2])  # banana (third element)

# Allows Duplicates
items = ["rice", "beans", "yam", "rice"]
print(items)   # ['rice', 'beans', 'yam', 'rice']

# Mutable(Can be changed - add elements, change elements or remove elements)
numbers = [1, 2, 3]
numbers[1] = 20
print(numbers)  # [1, 20, 3]

# Can Contain Different data types
mixed = [10, "Nigeria", 3.14, True]
print(mixed)   # [10, 'Nigeria', 3.14, True]

# Can be Nested - can contain other lists or multi-dimensional 
nested_list = [[1,2], ["a", "b"]]
print(nested_list)        # [[1, 2], ['a', 'b']]
print(nested_list[0][1])  # 2

# Dynamic size - It can grow or shrink as needed
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
print(names)  # ['Ada', 'Bola', 'Chidi']
