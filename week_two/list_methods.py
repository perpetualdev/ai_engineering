# ============ LIST METHODS =============
# Append 
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)
# Output: ['apple', 'banana', 'cherry']

# Insert
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)
# Output: ['apple', 'orange', 'banana']

# Extend
fruits = ["apple", "banana"]
tropical = ["mango", "pineapple"]
fruits.extend(tropical)
print(fruits)
# Output: ['apple', 'banana', 'mango', 'pineapple']

# Remove
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)
# Output: ['apple', 'cherry', 'banana']

# Pop - Remove and returns the element at a given index
fruits = ["apple", "banana", "cherry"]
# last_fruit = fruits.pop(1)
last_fruit = fruits.pop()
print(last_fruit)

# Clear
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
# Output: []

# Index
fruits = ["apple", "banana", "cherry"]
# position = fruits.index("mango")
# ValueError: 'mango' is not in list
position = fruits.index("banana")
print(position)

# Count
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))
# Output: 2

# Sort
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)
# Output: [1, 2, 3, 4]

# Descending Sort
numbers.sort(reverse=True)
print(numbers)
# Output: [4, 3, 2, 1]

# Reverse
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)
# Output: ['cherry', 'banana', 'apple']

# Copy
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)
# Output: ['apple', 'banana', 'cherry']
